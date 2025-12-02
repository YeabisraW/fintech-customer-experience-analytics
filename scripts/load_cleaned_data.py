import pandas as pd

# Load the cleaned CSV
df = pd.read_csv("data/cleaned/bank_reviews_clean.csv")

# Display the first 5 rows
print(df.head())

# Optional: print summary info
print(df.info())
print(df.describe())
