import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sentiment results

df = pd.read_csv("data/cleaned/bank_reviews_sentiment.csv")

# Example 1: Bar chart of sentiment counts per bank

plt.figure(figsize=(8,6))
sns.countplot(data=df, x='bank', hue='sentiment_label', palette='Set2')
plt.title("Sentiment Distribution per Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.show()

# Example 2: Boxplot of sentiment scores per bank

plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='bank', y='sentiment_score', palette='Set3')
plt.title("Sentiment Score Distribution per Bank")
plt.xlabel("Bank")
plt.ylabel("Sentiment Score")
plt.tight_layout()
plt.show()
