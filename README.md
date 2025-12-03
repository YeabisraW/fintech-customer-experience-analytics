# Fintech Customer Experience Analytics

This repository contains a workflow for analyzing customer reviews of Ethiopian banks using web scraping, sentiment analysis, thematic analysis, and driver/pain point analysis.

---

## **Project Structure**

```
data/
    raw/                # Raw scraped reviews
    cleaned/            # Cleaned and preprocessed CSVs
    processed/          # Sentiment scores, themes, and clustered outputs
    analysis/           # Plots, word clouds, and tables
scripts/
    scrape_reviews.py           # Task 1: Scrape Google Play reviews
    preprocess_reviews.py       # Task 1: Clean and preprocess reviews
    apply_vader_sentiment.py    # Task 2: Sentiment + Thematic Analysis pipeline
    sentiment_vader.py          # Optional: quick VADER sentiment test
    thematic_analysis.py        # Keyword extraction and thematic clustering
    theme_extraction.py         # Helper functions for theme grouping
    aggregate_sentiment.py      # Aggregates sentiment per bank or rating
    check_results.py            # Optional: preview sentiment and theme outputs
    task3_analysis.py           # Task 3: Early visualizations (sentiment distribution, ratings)
    task4_analysis.py           # Task 4: Drivers & Pain Points, word clouds
notebooks/        # Optional: Jupyter notebooks for exploration
analysis/         # Generated plots and word clouds
```

---

## **Workflow**

### **Task 1: Data Collection & Preprocessing**

1. **Scraping Reviews**

   * Run `scrape_reviews.py` to collect reviews from Google Play Store (≥400 per bank).
   * Raw reviews are saved to `data/raw/bank_reviews_raw.csv`.

2. **Cleaning & Preprocessing**

   * Run `preprocess_reviews.py` to remove duplicates, handle missing values, and normalize dates.
   * Cleaned reviews are saved to `data/cleaned/bank_reviews_clean.csv`.

---

### **Task 2: Sentiment and Thematic Analysis**

1. **Sentiment Analysis**

   * Run `apply_vader_sentiment.py` to compute VADER sentiment scores for all reviews.
   * Reviews are labeled `positive`, `negative`, or `neutral`.
   * Outputs saved to `data/processed/review_sentiment_vader.csv`.

2. **Keyword Extraction & Theme Clustering**

   * TF-IDF is used to extract top keywords per bank.

   * Keywords are mapped to predefined themes:

     * Account Access
     * Transaction Performance
     * UI & Experience
     * Customer Support
     * Feature Requests

   * Outputs saved to:

     * `data/processed/bank_themes.csv`
     * `data/processed/bank_themes_clustered.csv`

3. **Optional Checks**

   * Run `check_results.py` to preview sentiment distribution and theme assignments.

---

### **Task 3: Early Data Analysis & Visualizations**

* Run `task3_analysis.py` to generate initial exploratory visualizations:

  * **Sentiment distribution per bank** (`analysis/sentiment_distribution.png`)
  * **Average rating per bank** (`analysis/avg_rating_per_bank.png`)

* Quick insights for each bank’s review patterns and overall sentiment.

---

### **Task 4: Drivers & Pain Points Analysis**

* Run `task4_analysis.py` to identify top **positive drivers** and **negative pain points** per bank.

* Generate **word clouds** for the most frequent drivers and pain points:

  * `analysis/wordcloud_CBE_top.png`
  * `analysis/wordcloud_BOA_top.png`
  * `analysis/wordcloud_Dashen_top.png`

* Outputs also include **top 3 drivers and pain points with counts**, helping guide UX and feature improvements.

---

## **Sequential Workflow (How to Run All Tasks)**

1. **Task 1: Scraping & Cleaning**

```bash
python scripts/scrape_reviews.py
python scripts/preprocess_reviews.py
```

2. **Task 2: Sentiment & Thematic Analysis**

```bash
python scripts/apply_vader_sentiment.py
python scripts/thematic_analysis.py
python scripts/aggregate_sentiment.py
```

3. **Task 3: Exploratory Analysis**

```bash
python scripts/task3_analysis.py
```

4. **Task 4: Drivers & Pain Points**

```bash
python scripts/task4_analysis.py
```

---

## **KPIs / Minimum Essentials**

* Sentiment scores computed for 90%+ of reviews.
* At least 3 themes per bank with examples.
* Top drivers and pain points identified for each bank.
* Modular, reproducible pipeline code.
* Minimum: Sentiment for 400 reviews, 2 themes per bank, drivers/pain points analysis, committed scripts.

---

## **Dependencies**

* Python ≥3.10
* pandas
* matplotlib
* seaborn
* nltk
* scikit-learn
* wordcloud

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

This README fully documents **Tasks 1–4**, scripts, outputs, and analysis results.

