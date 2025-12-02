import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Functions
# -----------------------------

def load_cleaned_reviews(bank_name):
    """Load cleaned reviews CSV for a bank."""
    filepath = f"../data/cleaned/{bank_name}_reviews.csv"
    df = pd.read_csv(filepath)
    return df

def preprocess_text(df, column='content'):
    """Preprocess text: lowercase and remove NaN."""
    df = df.dropna(subset=[column])
    df[column] = df[column].str.lower()
    return df

def extract_tfidf_clusters(df, column='content', n_clusters=5):
    """Compute TF-IDF matrix and cluster reviews into themes."""
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(df[column])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)
    df['theme'] = clusters

    # Extract top keywords per cluster
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()
    cluster_keywords = {}
    for i in range(n_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :10]]
        cluster_keywords[i] = top_terms
    return df, cluster_keywords

def save_theme_results(df, bank_name, cluster_keywords):
    """Save clustered reviews and keywords to CSV and print summary."""
    os.makedirs("../data/analysis", exist_ok=True)
    df.to_csv(f"../data/analysis/{bank_name}_themes.csv", index=False)
    
    print(f"\nTop keywords per cluster for {bank_name}:")
    for cluster_id, keywords in cluster_keywords.items():
        print(f"Cluster {cluster_id}: {keywords}")

def plot_theme_distribution(df, bank_name):
    """Plot number of reviews per theme."""
    plt.figure(figsize=(6,4))
    sns.countplot(x='theme', data=df, palette='Set2')
    plt.title(f'{bank_name} - Theme Distribution')
    plt.xlabel("Theme Cluster")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    
    plot_dir = "../data/analysis/plots"
    os.makedirs(plot_dir, exist_ok=True)
    plt.savefig(f"{plot_dir}/{bank_name}_theme_distribution.png")
    plt.close()

# -----------------------------
# Main Pipeline
# -----------------------------
if __name__ == "__main__":
    banks = ['CBE', 'BOA', 'Dashen']
    for bank in banks:
        print(f"\nProcessing {bank} reviews...")
        df = load_cleaned_reviews(bank)
        df = preprocess_text(df)
        df, keywords = extract_tfidf_clusters(df, n_clusters=5)
        save_theme_results(df, bank, keywords)
        plot_theme_distribution(df, bank)
        print(f"{bank} thematic analysis complete.")
