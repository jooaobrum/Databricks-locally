import importlib
import subprocess
import sys
from pyspark.sql import SparkSession



def install_package(package):
    """Install a package using pip if it's not already installed."""
    try:
        importlib.import_module(package)
        print(f"'{package}' is already installed.")
    except ImportError:
        print(f"'{package}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Ensure pytest is installed
install_package('pytest')
import pytest


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """Creates a Spark session for use across tests."""
    try:
        return SparkSession.builder.appName("Test Session").getOrCreate()
    except Exception as e:
        print(f"Error creating Spark session: {e}")
        sys.exit(1)


@pytest.mark.parametrize("expected_count", [3095])
def test_spark_row_count(spark, expected_count):
    """
    Test if the row count in 'olist_silver.olist_sellers' is as expected.
    
    Args:
        spark (SparkSession): The Spark session for querying the database.
        expected_count (int): The expected row count in the table.
    """
    # Run a SQL query to get the row count
    try:
        row_count = spark.sql('SELECT COUNT(*) FROM olist_silver.olist_sellers').collect()[0][0]
        # Assert that the row count equals the expected value
        assert row_count == expected_count, f"Expected row count {expected_count}, but got {row_count}"
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        sys.exit(1)