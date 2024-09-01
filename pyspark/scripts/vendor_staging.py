from etl import ETL


class Vendor(ETL):
    def __init__(self, spark):
        self.spark = spark

    def extract(self):
        return self.spark.read.csv(
            "s3a://kanastra/raw/taxi/data-vendor_lookup.csv", header=True
        )

    def transform(self, vendor_lookup):
        return vendor_lookup

    def load(self, vendor_lookup):
        (
            vendor_lookup.write.format("delta")
            .mode("overwrite")
            .save("s3a://kanastra/staging/vendor-lookup/")
        )
