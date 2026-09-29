"""Query the mock MySQL database."""

import logging
import os

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# Read database settings from environment variables.
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))


def get_engine():
    """Create and return a connection engine for the database."""
    url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )

    return create_engine(url)


def get_data_by_group(value):
    """Return all rows where the `group` column equals value."""
    logger.info("Getting rows where group = %s", value)

    engine = get_engine()

    query = text("SELECT * FROM mock WHERE `group` = :value")

    with engine.connect() as connection:
        result = connection.execute(query, {"value": value})
        rows = result.fetchall()

    engine.dispose()

    logger.info("Found %d rows", len(rows))

    return rows


def plot_counts(groupby):
    """Count rows for each distinct value in the specified column."""
    logger.info("Counting rows by %s", groupby)

    engine = get_engine()

    # Column names cannot be parameterized, so groupby is inserted
    # into the SQL statement directly.
    query = text(
        f"SELECT `{groupby}`, COUNT(*) AS count "
        f"FROM mock "
        f"GROUP BY `{groupby}`"
    )

    with engine.connect() as connection:
        result = connection.execute(query)
        rows = result.fetchall()

    engine.dispose()

    logger.info("Found %d distinct values", len(rows))

    return rows


def main():
    """Run example queries against the mock database."""

    # Change this value to one of the actual group values in your data.
    rows = get_data_by_group("group1")
    print("Rows matching group1:")
    for row in rows:
        print(row)

    counts = plot_counts("group")
    print("\nCounts by group:")
    for row in counts:
        print(row)


if __name__ == "__main__":
    main()
