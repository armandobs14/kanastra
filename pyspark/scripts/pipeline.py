from functions import create_session

# Staging ETLs
from trip_staging import Trip as TripStaging
from vendor_staging import Vendor as VendorStaging
from trip_curated import Trip as TripCurated


if __name__ == "__main__":
    spark = create_session("Problem2")

    # crating staging area
    trip_staging_etl = TripStaging(spark)
    trip_staging_etl.run()

    vendor_staging_etl = VendorStaging(spark)
    vendor_staging_etl.run()

    # creating curated area
    trip_curated_etl = TripCurated(spark)
    trip_curated_etl.run()
