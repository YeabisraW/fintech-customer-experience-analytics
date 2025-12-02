import pandas as pd

# Load the cleaned reviews
df = pd.read_csv("data/cleaned/bank_reviews_clean.csv")

# Map bank names to numeric IDs
bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

# Add a new column for bank_id
df['bank_id'] = df['bank'].map(bank_mapping)

# Save back to the same CSV (or a new one)
df.to_csv("data/cleaned/bank_reviews_clean.csv", index=False)

print("Bank IDs added successfully!")
