import streamlit as st
import pandas as pd
import sqlite3
import os

# Page Config
st.set_page_config(page_title="Tech News Monitor", layout="wide")

# Database Path
DB_NAME = "scripts/news_data.db"  # Adjust if your DB is elsewhere


def load_data():
    conn = sqlite3.connect(DB_NAME)
    # Get the top 50 newest articles
    query = "SELECT * FROM hacker_news ORDER BY id DESC LIMIT 50"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --- DASHBOARD LAYOUT ---
st.title("Data Engineering Project: Tech News Tracker")
st.markdown("This dashboard monitors raw data scraped daily from YCombinator.")

# Refresh Button
if st.button('Refresh Data'):
    st.rerun()

# Load Data
try:
    df = load_data()

    # METRICS ROW
    col1, col2 = st.columns(2)
    col1.metric("Total Articles Scraped", len(df))
    col1.metric("Latest Source", "Hacker News")

    # SIMPLE ANALYTICS (e.g., Finding keyword trends)
    st.subheader("Keyword Analysis")
    search_term = st.text_input("Search for a keyword (e.g., 'AI', 'Google')")
    if search_term:
        filtered_df = df[df['title'].str.contains(search_term, case=False)]
        st.write(f"Found {len(filtered_df)} articles matching '{search_term}':")
        st.dataframe(filtered_df)

    # DATA TABLE
    st.subheader("Latest Headlines")
    # Show clean table without the internal ID
    st.dataframe(df[['rank', 'title', 'link', 'load_date']], use_container_width=True)



except Exception as e:
    st.error(f"Could not load database. Make sure the pipeline has run at least once! Error: {e}")