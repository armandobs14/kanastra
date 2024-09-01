from pyspark.sql.functions import max_by, rank, desc, col, broadcast, count
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from etl import ETL


class Trip(ETL):
    def __init__(self, spark):
        self.spark = spark

    def extract(self):
        return {
            "taxi_trips": self.spark.read.format("delta").load(
                "s3a://kanastra/staging/taxi-trips/"
            ),
            "vendor_lookup": self.spark.read.format("delta").load(
                "s3a://kanastra/staging/vendor-lookup/"
            ),
        }

    def transform(self, dfs):
        trips_by_year_week = (
            dfs["taxi_trips"]
            .groupBy("year", "year_week", "vendor_id")
            .agg(
                count("vendor_id").alias("trips"),
                F.sum("trip_distance").alias("total_distance"),
            )
        )

        week_df = trips_by_year_week.groupBy("year").agg(
            max_by("year_week", "trips").alias("year_week")
        )

        trips_by_year = trips_by_year_week.groupBy("year", "vendor_id").agg(
            F.sum("trips").alias("trips"),
            F.sum("total_distance").alias("total_distance"),
        )

        vendor_df = (
            trips_by_year.withColumn(
                "rank",
                rank().over(
                    Window.partitionBy("year").orderBy(
                        desc("trips"), desc("total_distance")
                    )
                ),
            )
            .filter(col("rank") == 1)
            .select("year", "vendor_id")
        )

        return (
            week_df.alias("week")
            .join(vendor_df.alias("vendor"), col("week.year") == col("vendor.year"))
            .join(
                trips_by_year_week.alias("trips"),
                (col("trips.year") == col("vendor.year"))
                & (col("trips.year_week") == col("week.year_week"))
                & (col("trips.vendor_id") == col("vendor.vendor_id")),
            )
            .join(
                broadcast(dfs["vendor_lookup"]).alias("lookup"),
                col("lookup.vendor_id") == col("vendor.vendor_id"),
            )
            .select("week.year", "week.year_week", "lookup.name", "trips.trips")
        )

    def load(self, final_df):
        final_df.coalesce(1).write.mode("overwrite").csv(
            "s3a://kanastra/curated/taxi-trips.csv", header=True
        )
