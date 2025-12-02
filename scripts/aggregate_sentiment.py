import pandas as pd

# Load the sentiment CSV
df = pd.read_csv("data/cleaned/bank_reviews_sentiment.csv")

# --- 1. Average sentiment per bank ---
bank_sentiment = df.groupby('bank')['sentiment_score'].mean().sort_values(ascending=False)
print("Average sentiment per bank:")
print(bank_sentiment)

# --- 2. Average sentiment per bank AND rating ---
bank_rating_sentiment = df.groupby(['bank', 'rating'])['sentiment_score'].mean().unstack()
print("\nAverage sentiment per bank and rating:")
print(bank_rating_sentiment)

# --- 3. Optional: save aggregated results ---
bank_sentiment.to_csv("data/cleaned/aggregate_bank_sentiment.csv")
bank_rating_sentiment.to_csv("data/cleaned/aggregate_bank_rating_sentiment.csv")
print("\nAggregated results saved!")
