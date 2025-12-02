import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Load sentiment-scored reviews
df = pd.read_csv("data/cleaned/bank_reviews_sentiment.csv")
print(f"Loaded {len(df)} reviews")

# Step 2: Basic preprocessing
df['review'] = df['review'].fillna("").str.lower()

# Step 3: Extract top keywords using TF-IDF (optional display)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=50)
X = vectorizer.fit_transform(df['review'])
keywords = vectorizer.get_feature_names_out()
print("Top keywords:", keywords)

# Step 4: Assign themes manually
def assign_theme(review):
    if any(word in review for word in ["login", "password", "access"]):
        return "Account Access Issues"
    elif any(word in review for word in ["slow", "transfer", "delay"]):
        return "Transaction Performance"
    elif any(word in review for word in ["ui", "interface", "layout"]):
        return "User Interface & Experience"
    elif any(word in review for word in ["support", "help", "customer service"]):
        return "Customer Support"
    else:
        return "Other"

df['identified_theme'] = df['review'].apply(assign_theme)

# Step 5: Save themed CSV
df.to_csv("data/cleaned/bank_reviews_themes.csv", index=False)
print("Saved themes to data/cleaned/bank_reviews_themes.csv")
