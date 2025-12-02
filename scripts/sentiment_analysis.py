import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load cleaned CSV
df = pd.read_csv("data/cleaned/bank_reviews_clean.csv")

# Initialize sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Prepare columns
df['sentiment_label'] = ""
df['sentiment_score'] = 0.0

# Process reviews with progress bar
for i, review in tqdm(enumerate(df['review']), total=len(df)):
    try:
        result = sentiment_pipeline(str(review))[0]
        df.at[i, 'sentiment_label'] = result['label']
        df.at[i, 'sentiment_score'] = result['score']
    except Exception as e:
        df.at[i, 'sentiment_label'] = "ERROR"
        df.at[i, 'sentiment_score'] = 0.0

# Save the sentiment CSV
df.to_csv("data/cleaned/bank_reviews_sentiment.csv", index=False)
print("Sentiment analysis completed!")
