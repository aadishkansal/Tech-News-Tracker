import requests
import os
from datetime import datetime

# 1. Define the URL and the storage location
URL = "https://news.ycombinator.com/"
SAVE_DIR = "../raw_data"  # Relative path to your Data Lake folder

# 2. Ensure the directory exists (Good engineering practice)
os.makedirs(SAVE_DIR, exist_ok=True)

# 3. The "User-Agent" Header (Faking a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def extract_html():
    try:
        print(f"Attempting to fetch data from {URL}...")

        # Send the request
        response = requests.get(URL, headers=headers)

        # Check if request was successful (Status Code 200 = OK)
        if response.status_code == 200:
            # Generate a filename with a TIMESTAMP
            # Why? So we never overwrite yesterday's data. This builds history.
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hacker_news_raw_{timestamp}.html"
            filepath = os.path.join(SAVE_DIR, filename)

            # Save the RAW HTML content
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"SUCCESS: Data saved to {filepath}")
        else:
            print(f"FAILED: Status Code {response.status_code}")

    except Exception as e:
        print(f"ERROR: An exception occurred - {e}")


if __name__ == "__main__":
    extract_html()