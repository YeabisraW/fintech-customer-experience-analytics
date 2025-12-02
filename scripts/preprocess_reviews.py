import pandas as pd

# Load raw reviews
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

# Remove duplicates and missing reviews
df.drop_duplicates(subset="review", inplace=True)
df.dropna(subset=["review"], inplace=True)

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.date

# Save cleaned data
df.to_csv("data/cleaned/bank_reviews_clean.csv", index=False)
print("Preprocessing done!")
