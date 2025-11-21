import pandas as pd

import extract_news
import transform_news
import load_to_db
import time
from datetime import datetime, timedelta

# Define the End Date (2 weeks from now)
START_DATE = datetime(2025, 11, 21) # Set this to today
END_DATE = START_DATE + timedelta(days=14)


def run_pipeline():
    print("=================================")
    print("   STARTING DAILY DATA PIPELINE  ")
    print("=================================")

    # Step 1: Extract
    print("\n[STEP 1] Starting Extraction...")
    extract_news.extract_html()

    # Optional: Wait a second to ensure file write completes
    time.sleep(1)

    # Step 2: Transform
    print("\n[STEP 2] Starting Transformation...")
    # We need to modify transform to return the data or just run the logic
    # Since our scripts have "if __name__ == '__main__':", importing them
    # doesn't run the logic automatically. We need to call the functions directly.

    # Note: We need to slightly adjust transform_news.py to be callable
    # Or we can just call the main logic if we refactored slightly.
    # For now, let's assume we call the functions we defined:

    latest_file = transform_news.get_latest_file()
    if latest_file:
        data = transform_news.parse_html(latest_file)
        df = pd.DataFrame(data)
        df.to_csv(f"../processed_data/hacker_news_cleaned.csv", index=False)
        print("Transformation Complete.")

    # Step 3: Load
    print("\n[STEP 3] Starting Load...")
    load_to_db.save_to_database()

    print("\n=================================")
    print("   PIPELINE FINISHED SUCCESSFULLY ")
    print("=================================")


if __name__ == "__main__":
    run_pipeline()