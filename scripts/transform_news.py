import os
import glob
import pandas as pd
from bs4 import BeautifulSoup

# Define directories
RAW_DIR = "../raw_data"
PROCESSED_DIR = "../processed_data"
os.makedirs(PROCESSED_DIR, exist_ok=True)


def get_latest_file():
    """Finds the most recently created file in the raw_data folder."""
    # glob.glob gets a list of all files matching the pattern
    list_of_files = glob.glob(os.path.join(RAW_DIR, "*.html"))

    if not list_of_files:
        return None

    # Sort files by creation time and pick the last one (latest)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def parse_html(file_path):
    print(f"Processing file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    extracted_data = []

    # HACKER NEWS STRUCTURE (This is the tricky part!)
    # Hacker News uses a table structure.
    # The titles are in rows with class="athing".

    articles = soup.find_all("tr", class_="athing")

    for article in articles:
        try:
            # 1. Extract Rank (e.g., "1.")
            rank_text = article.find("span", class_="rank").text.replace(".", "")

            # 2. Extract Title and Link
            title_tag = article.find("span", class_="titleline").find("a")
            title = title_tag.text
            link = title_tag["href"]

            # 3. Store in a dictionary
            row = {
                "rank": rank_text,
                "title": title,
                "link": link
            }
            extracted_data.append(row)

        except AttributeError:
            # If a row is missing data, skip it (Good Error Handling)
            continue

    return extracted_data


if __name__ == "__main__":
    # 1. Get the raw data
    latest_file = get_latest_file()

    if latest_file:
        # 2. Transform the data
        data = parse_html(latest_file)

        # 3. Load into a DataFrame (Structured Table)
        df = pd.DataFrame(data)

        # 4. Save to Processed folder (The "Warehouse")
        output_filename = "hacker_news_cleaned.csv"
        output_path = os.path.join(PROCESSED_DIR, output_filename)

        df.to_csv(output_path, index=False)

        print(f"SUCCESS: Extracted {len(df)} rows.")
        print(f"Data saved to: {output_path}")
        print("Preview:")
        print(df.head())  # Show the first 5 rows
    else:
        print("No raw files found! Run the extraction script first.")