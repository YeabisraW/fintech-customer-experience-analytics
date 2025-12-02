# Fintech Customer Experience Analytics

This repository contains a workflow for analyzing customer reviews of Ethiopian banks using web scraping, sentiment analysis, and thematic analysis.

---

## **Project Structure**

```
data/
    raw/                # Raw scraped reviews
    cleaned/            # Cleaned and preprocessed CSVs
    processed/          # Sentiment scores, themes, and clustered outputs
    analysis/           # Optional folder for plots or tables
scripts/
    scrape_reviews.py           # Task 1: Scrape Google Play reviews
    preprocess_reviews.py       # Task 1: Clean and preprocess reviews
    apply_vader_sentiment.py    # Task 2: Sentiment + Thematic Analysis pipeline
    sentiment_vader.py          # Optional: quick VADER sentiment test
    thematic_analysis.py        # Keyword extraction and thematic clustering
    theme_extraction.py         # Helper functions for theme grouping
    aggregate_sentiment.py      # Aggregates sentiment per bank or rating
    check_results.py            # Optional: preview sentiment and theme outputs
notebooks/        # Optional: Jupyter notebooks for exploration
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

## **KPIs / Minimum Essential**

* Sentiment scores computed for 90%+ of reviews.
* At least 3 themes per bank with examples.
* Modular, reproducible pipeline code.
* Minimum: Sentiment for 400 reviews, 2 themes per bank, committed scripts.

---

## **Dependencies**

* Python ≥3.10
* pandas
* nltk
* scikit-learn

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

This README now documents both **Task 1 & 2**, your scripts, and data outputs — ready for review or merging.
