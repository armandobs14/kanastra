from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
import os


def create_session(app_name):
    """Create preconfigured spark session

    Args:
        app_name str: Spark application Name

    Returns:
        SparkSession: spark session
    """
    minio_host = os.getenv("MINIO_HOSTNAME", "minio")
    host_url = f"http://{minio_host}:9000/"

    packages = [
        "com.amazonaws:aws-java-sdk-bundle:1.12.728",
        "org.apache.hadoop:hadoop-aws:3.3.2",
        "io.delta:delta-spark_2.13:3.2.0",
        "org.apache.spark:spark-catalyst_2.13:3.3.2",
    ]

    conf = SparkConf()
    conf.set("spark.jars.packages", ",".join(packages))
    conf.set(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
    conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    conf.set("spark.sql.shuffle.partitions", "4")
    conf.set("spark.hadoop.fs.s3a.endpoint", host_url)
    conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    conf.set("spark.hadoop.fs.s3a.path.style.access", "true")

    return (
        SparkSession.builder.appName(app_name)
        .master("local[*]")
        .config(conf=conf)
        .getOrCreate()
    )
