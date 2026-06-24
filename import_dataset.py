import sqlite3
from pathlib import Path

import pandas as pd


CSV_PATH = Path("data/hoax_data_final.csv")
DATABASE_PATH = Path("database.db")


def main():
    df = pd.read_csv(CSV_PATH)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS information (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        source TEXT NOT NULL,
        topic TEXT NOT NULL,
        publication_date TEXT NOT NULL,
        label TEXT NOT NULL
    )
    """)

    cursor.execute("DELETE FROM information")

    df.to_sql(
        "information",
        connection,
        if_exists="append",
        index=False
    )

    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM information")
    total_data = cursor.fetchone()[0]

    connection.close()

    print("Dataset imported successfully.")
    print(f"Total data inserted: {total_data}")


if __name__ == "__main__":
    main()