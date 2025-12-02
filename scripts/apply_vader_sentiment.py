import os
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# ------------------------

# Step 0: Download VADER lexicon

nltk.download('vader_lexicon')

# ------------------------

# Step 1: Load cleaned reviews

df = pd.read_csv("data/cleaned/bank_reviews_clean.csv")

# ------------------------

# Step 2: Sentiment Analysis with VADER

sid = SentimentIntensityAnalyzer()
df['sentiment_score'] = df['review'].apply(lambda x: sid.polarity_scores(str(x))['compound'])

def label_sentiment(score):
 if score >= 0.05:
  return 'positive'
 elif score <= -0.05:
  return 'negative'
 else:
  return 'neutral'

df['sentiment_label'] = df['sentiment_score'].apply(label_sentiment)

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/review_sentiment_vader.csv", index=False)
print("Sentiment analysis completed! CSV saved to data/processed/review_sentiment_vader.csv")

# ------------------------

# Step 3: Keyword Extraction with TF-IDF

vectorizer = TfidfVectorizer(max_df=0.8, min_df=5, ngram_range=(1,2), stop_words='english')
X = vectorizer.fit_transform(df['review'].astype(str))
keywords = vectorizer.get_feature_names_out()

themes = []
for bank in df['bank'].unique():
 bank_reviews = df[df['bank'] == bank]
 bank_X = vectorizer.transform(bank_reviews['review'].astype(str))
 tfidf_sum = bank_X.sum(axis=0)
 tfidf_scores = [(keywords[i], tfidf_sum[0, i]) for i in range(len(keywords))]
 tfidf_scores.sort(key=lambda x: x[1], reverse=True)
 top_keywords = [kw for kw, score in tfidf_scores[:20]]  # top 20 keywords
 themes.append({'bank': bank, 'top_keywords': top_keywords})

pd.DataFrame(themes).to_csv("data/processed/bank_themes.csv", index=False)
print("Keyword extraction and theme CSV saved to data/processed/bank_themes.csv")

# ------------------------

# Step 4: Theme Clustering

df_themes = pd.read_csv("data/processed/bank_themes.csv")

theme_map = {
'Account Access': ['login', 'password', 'otp', 'access', 'blocked'],
'Transaction Performance': ['slow', 'transfer', 'payment', 'failed', 'processing'],
'UI & Experience': ['ui', 'user', 'interface', 'design', 'easy'],
'Customer Support': ['support', 'help', 'service', 'response', 'chat'],
'Feature Requests': ['feature', 'update', 'fingerprint', 'biometric', 'request']
}

def assign_themes(keywords):
 assigned = []
 for theme, words in theme_map.items():
  if any(word in keywords for word in words):
   assigned.append(theme)
   return assigned

df_themes['themes'] = df_themes['top_keywords'].apply(lambda kws: assign_themes(str(kws)))
df_themes.to_csv("data/processed/bank_themes_clustered.csv", index=False)
print("Theme clustering completed! CSV saved to data/processed/bank_themes_clustered.csv")

