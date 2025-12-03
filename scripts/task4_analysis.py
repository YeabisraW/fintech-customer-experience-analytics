import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# ------------------------------
# Ensure 'analysis' folder exists
# ------------------------------
os.makedirs("analysis", exist_ok=True)

# ------------------------------
# Step 1: Load the CSV
# ------------------------------
df = pd.read_csv("data/cleaned/bank_reviews_sentiment.csv")

# ------------------------------
# Step 2: Quick Data Checks
# ------------------------------
print(df.info())
print(df['bank'].value_counts())
print(df['sentiment_label'].value_counts())

# ------------------------------
# Step 3: Sentiment Distribution per Bank
# ------------------------------
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='bank', hue='sentiment_label', order=['CBE','BOA','Dashen'])
plt.title('Sentiment Distribution per Bank')
plt.ylabel('Number of Reviews')
plt.xlabel('Bank')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig("analysis/sentiment_distribution.png")
plt.show()

# ------------------------------
# Step 4: Average Rating per Bank
# ------------------------------
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='bank', y='rating', order=['CBE','BOA','Dashen'])
plt.title('Average Rating per Bank')
plt.ylabel('Average Rating')
plt.xlabel('Bank')
plt.tight_layout()
plt.savefig("analysis/avg_rating_per_bank.png")
plt.show()

# ------------------------------
# Step 5: Drivers and Pain Points (with counts)
# ------------------------------
drivers_painpoints = {}

positive_words = ['good','easy','fast','friendly','best','smooth','quick','helpful']
negative_words = ['slow','crash','problem','error','bug','difficult','lag','fail']

for bank_name in df['bank'].unique():
    reviews_text = df[df['bank'] == bank_name]['review'].astype(str).tolist()
    all_words = ' '.join(reviews_text).lower().split()
    word_counts = Counter(all_words)
    
    driver_counts = {word: word_counts[word] for word in positive_words if word in word_counts}
    painpoint_counts = {word: word_counts[word] for word in negative_words if word in word_counts}
    
    top_drivers = sorted(driver_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    top_painpoints = sorted(painpoint_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    
    drivers_painpoints[bank_name] = {
        'drivers': top_drivers,
        'painpoints': top_painpoints
    }

print("\nDrivers and Pain Points per Bank with Counts:")
for bank, info in drivers_painpoints.items():
    print(f"{bank}:")
    print(f"  Drivers: {info['drivers']}")
    print(f"  Pain Points: {info['painpoints']}")

# ------------------------------
# Step 6: Word Clouds using top drivers/pain points
# ------------------------------
for bank_name in df['bank'].unique():
    text = []
    for word, count in drivers_painpoints[bank_name]['drivers'] + drivers_painpoints[bank_name]['painpoints']:
        text.extend([word] * count)
    text_str = ' '.join(text)

    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=50).generate(text_str)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Top Drivers & Pain Points in {bank_name} Reviews')
    plt.tight_layout()
    plt.savefig(f"analysis/wordcloud_{bank_name}_top.png")
    plt.show()
    print(f"Word cloud saved: analysis/wordcloud_{bank_name}_top.png")
