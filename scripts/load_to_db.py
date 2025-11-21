import pandas as pd
import sqlite3
import os

# Define paths
PROCESSED_DIR = "../processed_data"
DB_NAME = "news_data.db"
CSV_FILENAME = "hacker_news_cleaned.csv"


def save_to_database():
    csv_path = os.path.join(PROCESSED_DIR, CSV_FILENAME)

    if not os.path.exists(csv_path):
        print("ERROR: CSV file not found.")
        return

    # 1. Read the New Data
    new_df = pd.read_csv(csv_path)
    print(f"Read {len(new_df)} rows from CSV.")

    # 2. Connect to Database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Table (Same as before)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hacker_news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rank TEXT,
        title TEXT,
        link TEXT,
        load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 3. GET EXISTING LINKS (The Logic Check)
    # We query only the 'link' column to check what we already have.
    try:
        existing_links_df = pd.read_sql("SELECT link FROM hacker_news", conn)
        existing_links = set(existing_links_df['link'].tolist())
    except:
        existing_links = set()  # If table is empty/new

    # 4. FILTER: Keep only rows where the link is NOT in existing_links
    # This is a standard Pandas filtering technique
    rows_to_insert = new_df[~new_df['link'].isin(existing_links)]

    if rows_to_insert.empty:
        print("No new data found. Database is up to date.")
    else:
        # 5. Load only the new rows
        rows_to_insert.to_sql('hacker_news', conn, if_exists='append', index=False)
        print(f"SUCCESS: Added {len(rows_to_insert)} NEW rows to the Database.")

    conn.close()


if __name__ == "__main__":
    save_to_database()