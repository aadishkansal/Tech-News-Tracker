# 📰 Tech News Tracker  
### Automated Hacker News Scraper & ETL Pipeline (Python + SQL + Local Data Lake)

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![SQL](https://img.shields.io/badge/Database-SQLite-green.svg)
![Scraper](https://img.shields.io/badge/Type-Web%20Scraper-orange.svg)
![Pipeline](https://img.shields.io/badge/ETL-Pipeline-blueviolet.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📌 Overview  
**Tech News Tracker** is a complete ETL pipeline that extracts the latest tech stories from  
**Hacker News (Y Combinator)** → transforms the data → loads it into an SQL database → and generates a clean processed dataset.

It uses:  
- **Python** for scraping & transformation  
- **Local Data Lake** for storing raw & processed files  
- **SQLite** for database storage  
- **Modular ETL scripts** for pipeline automation  

Perfect for **data engineering practice, automation workflows, and portfolio building**.

---

## 📂 Project Structure  

data_engineering_project/
│
├── processed_data/
│   └── hacker_news_cleaned.csv       # Processed & cleaned dataset
│
├── raw_data/                         # Raw scraped data (JSON/HTML)
│
├── scripts/
│   ├── extract_news.py               # Extract step: scrapes Hacker News
│   ├── transform_news.py             # Transform step: cleaning & structuring
│   ├── load_to_db.py                 # Load step: inserts into SQLite DB
│   ├── pipeline_controller.py        # Runs Extract → Transform → Load automatically
│   ├── dashboard.py                  # Optional dashboard for viewing data
│   └── news_data.db                  # SQLite database file
│
├── requirements.txt
└── README.md

---

## 🚀 Features  
- 🔍 Extracts real-time top articles from **Hacker News**  
- 📦 Stores raw data inside a **local data lake** (`raw_data/`)  
- 🧹 Cleans & transforms the data (`processed_data/`)  
- 🛢 Loads everything into **SQLite database** (`news_data.db`)  
- 🔄 Fully automated ETL using `pipeline_controller.py`  
- 📊 Optional dashboard for visualizing the news  
- 🧩 Modular design — easy to extend or plug into other systems  

---

## 🧰 Tech Stack  
- **Python 3.11**  
- **Requests + BeautifulSoup**  
- **Pandas**  
- **SQLite (via `sqlite3`)**  
- **Local storage data lake**  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/tech-news-tracker.git
cd tech-news-tracker

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the ETL pipeline

python scripts/pipeline_controller.py

4️⃣ Run components separately (optional)

Extract:

python scripts/extract_news.py

Transform:

python scripts/transform_news.py

Load:

python scripts/load_to_db.py

Dashboard:

python scripts/dashboard.py


⸻

🗄 Database

Project uses SQLite stored at:

scripts/news_data.db

You can query it using tools like DB Browser or Python.

⸻

📅 Automate the Pipeline

Cron (Mac/Linux):

0 * * * * python /path/to/scripts/pipeline_controller.py

Windows Task Scheduler:
	•	Create a task → point to pipeline_controller.py.

⸻

📚 Use Cases
	•	Data engineering practice
	•	ETL/ELT pipelines
	•	Web scraping automation
	•	Portfolio showcase
	•	Research datasets
	•	Dashboards & analytics

⸻

🤝 Contributing

Pull requests and improvements are welcome.
Open an issue if you’d like to add new sources or features.

⸻

📜 License

This project is licensed under the MIT License.

