from google_play_scraper import Sort, reviews
import pandas as pd
import time
import os

# Banks with Google Play package IDs
banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

OUTPUT_PATH = "data/cleaned/bank_reviews_clean.csv"
TARGET_REVIEWS = 450  # ensures >400
BATCH = 200

os.makedirs("data/cleaned", exist_ok=True)

# Load existing reviews or create empty DataFrame
if os.path.exists(OUTPUT_PATH):
    df_existing = pd.read_csv(OUTPUT_PATH)
else:
    df_existing = pd.DataFrame()

all_banks_df = []

for bank_name, pkg in banks.items():
    print(f"\n🔍 Scraping reviews for {bank_name}...")

    # Load existing bank reviews
    if not df_existing.empty:
        df_bank_existing = df_existing[df_existing["bank"] == bank_name]
        collected = df_bank_existing.to_dict("records")
    else:
        df_bank_existing = pd.DataFrame()
        collected = []

    continuation_token = None

    while len(collected) < TARGET_REVIEWS:
        rvws, continuation_token = reviews(
            pkg,
            count=BATCH,
            sort=Sort.NEWEST,
            continuation_token=continuation_token
        )

        if not rvws:
            print(f"⚠ No more reviews available for {bank_name}.")
            break

        collected.extend(rvws)
        print(f"  → Collected so far: {len(collected)}")
        time.sleep(1)  # prevent rate limiting

    # Convert to DataFrame
    df_bank = pd.DataFrame(collected)
    df_bank["bank"] = bank_name
    all_banks_df.append(df_bank)

# Combine with previous & remove duplicates
df_all = pd.concat(all_banks_df, ignore_index=True)

if not df_existing.empty:
    df_all = pd.concat([df_existing, df_all], ignore_index=True)

# Remove duplicates based on review text
df_all.drop_duplicates(subset=["content"], inplace=True)

# Normalize date
if "at" in df_all.columns:
    df_all["at"] = pd.to_datetime(df_all["at"]).dt.strftime("%Y-%m-%d")

# Handle missing values
df_all.fillna("", inplace=True)

# Save
df_all.to_csv(OUTPUT_PATH, index=False)

print("\n🎉 FINAL REVIEW COUNTS:")
print(df_all["bank"].value_counts())

