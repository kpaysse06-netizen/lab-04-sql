"""Read a CSV, clean it, and upload it to a MySQL table named "mock"."""
 
import logging
import os
 
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
 
# Configure logging so every function can report its status
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
 
# Database settings come from environment variables (never hard-code secrets)
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))  # optional, MySQL default
 
CSV_FILE = "MOCK_DATA.csv"
TABLE_NAME = "mock"  # always "mock" so it is consistent across all databases
 
 
def read_data(filename):
    """Load a CSV file into a pandas DataFrame and return it."""
    logger.info("Reading data from %s", filename)
    df = pd.read_csv(filename)
    logger.info("Read %d rows and %d columns", df.shape[0], df.shape[1])
    return df
 
 
def clean_data(data):
    """Remove rows with missing values and return the cleaned DataFrame."""
    logger.info("Cleaning data (starting with %d rows)", len(data))
    # Drop any row that has at least one missing value
    cleaned = data.dropna().reset_index(drop=True)
    logger.info(
        "Removed %d rows with missing values; %d rows remain",
        len(data) - len(cleaned),
        len(cleaned),
    )
    return cleaned
 
 
def load_data(data, table):
    """Write a DataFrame to the given MySQL table, creating it if needed."""
    # Make sure all connection settings were provided
    missing = [
        name
        for name, value in [
            ("DB_HOST", DB_HOST),
            ("DB_NAME", DB_NAME),
            ("DB_USER", DB_USER),
            ("DB_PASSWORD", DB_PASSWORD),
        ]
        if not value
    ]
    if missing:
        logger.error("Missing environment variables: %s", ", ".join(missing))
        raise SystemExit(1)
 
    engine = None
    try:
        # URL.create builds mysql+mysqlconnector://USER:PASS@HOST:PORT/DBNAME
        # and safely escapes special characters in the password
        url = URL.create(
            drivername="mysql+mysqlconnector",
            username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )
        engine = create_engine(url)
        logger.info("Uploading %d rows to table '%s'", len(data), table)
 
        # to_sql creates the table if it doesn't exist and inserts all rows
        # (if_exists="append" keeps any existing table and adds to it)
        data.to_sql(table, con=engine, if_exists="append", index=False)
        logger.info("Upload to '%s' succeeded", table)
    except Exception as exc:
        logger.error("Upload failed: %s", exc)
        raise
    finally:
        # Always close the connection pool, even if the upload failed
        if engine is not None:
            engine.dispose()
            logger.info("Database connection closed")
 
 
def main():
    """Run the pipeline: read, clean, then load the data."""
    logger.info("Starting pipeline")
    df = read_data(CSV_FILE)
    df = clean_data(df)
    load_data(df, TABLE_NAME)
    logger.info("Pipeline finished")
 
 
if __name__ == "__main__":
    main()
