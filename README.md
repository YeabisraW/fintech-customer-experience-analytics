# fintech-customer-experience-analytics

## Project Overview

This project analyzes customer satisfaction for Ethiopian mobile banking apps by collecting and processing user reviews from the Google Play Store. It focuses on three banks:

* **Commercial Bank of Ethiopia (CBE)**
* **Bank of Abyssinia (BOA)**
* **Dashen Bank**

The goal is to extract insights from user feedback to guide app improvements, enhance user retention, and support fintech strategies.

---

## Learning Objectives

By completing this project, you will be able to:

* Scrape and preprocess user reviews from the Google Play Store.
* Apply NLP techniques to analyze review sentiment and extract themes.
* Design a relational database schema in Postgres to manage review data.
* Generate visualizations and actionable insights for stakeholders.
* Use Git for version control and write unit tests to ensure script reliability.

---

## Project Structure

```
fintech-customer-experience-analytics/
├── data/                  # Raw and cleaned datasets (add to .gitignore)
├── scripts/               # Python scripts for scraping & preprocessing
├── notebooks/             # Jupyter notebooks for analysis & visualization
├── requirements.txt       # Python dependencies
├── .gitignore             # Exclude data, env, etc.
└── README.md              # Project documentation
```

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/YeabisraW/fintech-customer-experience-analytics.git
cd fintech-customer-experience-analytics
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Scrape Reviews

Run
