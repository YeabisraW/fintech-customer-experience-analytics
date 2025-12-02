from google_play_scraper import reviews, Sort
import pandas as pd
import os

# -----------------------------
# Config
# -----------------------------
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

output_dir = "../data/raw"
os.makedirs(output_dir, exist_ok=True)  # create folder if not exists

# -----------------------------
# Scrape reviews
# -----------------------------
for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")
    
    # Scrape 500 latest reviews
    rvs, _ = reviews(
        app_id,
        lang='en',           # English reviews
        count=500,           # Number of reviews to scrape
        sort=Sort.NEWEST
    )
    
    # Convert to DataFrame
    df = pd.DataFrame(rvs)
    
    # Save to CSV
    csv_path = os.path.join(output_dir, f"{bank}_reviews_raw.csv")
    df.to_csv(csv_path, index=False)
    
    print(f"Saved {len(df)} reviews for {bank} to {csv_path}\n")
