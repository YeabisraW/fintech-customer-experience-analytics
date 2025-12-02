import pandas as pd

# Load sentiment results
df_sentiment = pd.read_csv("data/processed/review_sentiment_vader.csv")
print(df_sentiment[['review','sentiment_label','sentiment_score']].head())

# Load clustered themes
df_themes = pd.read_csv("data/processed/bank_themes_clustered.csv")
print(df_themes.head())
