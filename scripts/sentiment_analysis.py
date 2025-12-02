import pandas as pd
from transformers import pipeline

# Load cleaned reviews
df = pd.read_csv("data/cleaned/bank_reviews_clean.csv")

# Initialize sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to get sentiment label and score
def get_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # truncate long reviews
        label = result['label']  # 'POSITIVE' or 'NEGATIVE'
        score = result['score']
        if score < 0.6:
            label = "NEUTRAL"
        return label, score
    except:
        return "NEUTRAL", 0.0

# Apply sentiment analysis
df['sentiment_label'], df['sentiment_score'] = zip(*df['review'].map(get_sentiment))

# Save new CSV
df.to_csv("data/cleaned/bank_reviews_sentiment.csv", index=False)
print("Sentiment analysis completed!")
