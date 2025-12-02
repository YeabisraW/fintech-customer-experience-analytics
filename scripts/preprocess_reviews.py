import pandas as pd
import os

# Paths
RAW_PATH = "data/cleaned/bank_reviews_clean.csv"
FINAL_PATH = "data/cleaned/bank_reviews_final.csv"

# Load the scraped data
df = pd.read_csv(RAW_PATH)

print(f"Initial review counts per bank:\n{df['bank'].value_counts()}")

# 1️⃣ Remove duplicates based on review content
df.drop_duplicates(subset=["content"], inplace=True)

# 2️⃣ Handle missing review text
df = df[df["content"].notna() & (df["content"].str.strip() != "")]

# 3️⃣ Normalize date format
if "at" in df.columns:
    df["at"] = pd.to_datetime(df["at"], errors="coerce")  # convert to datetime
    df = df[df["at"].notna()]  # drop invalid dates
    df["at"] = df["at"].dt.strftime("%Y-%m-%d")  # standard YYYY-MM-DD format

# 4️⃣ Ensure bank label exists
if "bank" not in df.columns:
    df["bank"] = "Unknown"

# 5️⃣ Reset index
df.reset_index(drop=True, inplace=True)

# 6️⃣ Save final cleaned CSV
os.makedirs(os.path.dirname(FINAL_PATH), exist_ok=True)
df.to_csv(FINAL_PATH, index=False)

print(f"\n✅ Preprocessing complete! Cleaned CSV saved at: {FINAL_PATH}")
print(f"\nFinal review counts per bank:\n{df['bank'].value_counts()}")

