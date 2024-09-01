from pyspark.sql.functions import to_timestamp, year, weekofyear
from etl import ETL


class Trip(ETL):
    def __init__(self, spark):
        self.spark = spark

    def extract(self):
        return self.spark.read.json("s3a://kanastra/raw/taxi/data-nyctaxi-trips-*.json")

    def transform(self, trips_df):
        return (
            trips_df.withColumn("dropoff_datetime", to_timestamp("dropoff_datetime"))
            .withColumn("pickup_datetime", to_timestamp("pickup_datetime"))
            .withColumn("year", year("pickup_datetime"))
            .withColumn("year_week", weekofyear("pickup_datetime"))
        )

    def load(self, trips_df):
        (
            trips_df.write.format("delta")
            .partitionBy("year", "year_week")
            .mode("overwrite")
            .save("s3a://kanastra/staging/taxi-trips/")
        )
