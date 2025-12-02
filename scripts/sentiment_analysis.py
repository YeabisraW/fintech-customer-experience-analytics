# Task 2 – Sentiment and Thematic Analysis

# Step 1: Load cleaned data
import pandas as pd
df = pd.read_csv("data/cleaned/bank_reviews_final.csv")
print("Loaded data. Number of reviews per bank:")
print(df['bank'].value_counts())

# Step 2: Sentiment Analysis using VADER
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
df['sentiment_score'] = df['content'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment'] = df['sentiment_score'].apply(lambda x: 'POSITIVE' if x >= 0 else 'NEGATIVE')
print("\nSample sentiment results:")
print(df[['content','sentiment','sentiment_score']].head())

# Step 3: Keyword/Thematic Extraction using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

themes_per_bank = {}
for bank in df['bank'].unique():
    reviews = df[df['bank'] == bank]['content'].tolist()
    vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
    X = vectorizer.fit_transform(reviews)
    keywords = vectorizer.get_feature_names_out()
    themes_per_bank[bank] = keywords

print("\nTop keywords per bank:")
for bank, keywords in themes_per_bank.items():
    print(f"{bank}: {keywords}")

# Step 4: Optional clustering into themes
from sklearn.cluster import KMeans

for bank in df['bank'].unique():
    reviews = df[df['bank'] == bank]['content']
    vectorizer = TfidfVectorizer(stop_words='english', max_features=50)
    X = vectorizer.fit_transform(reviews)
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)
    print(f"\n{bank} review cluster labels (first 10): {kmeans.labels_[:10]}")

# Step 5: Save results
df.to_csv("data/cleaned/bank_reviews_sentiment.csv", index=False)
print("\nSentiment analysis results saved to 'bank_reviews_sentiment.csv'")
