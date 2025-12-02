from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")
    rvs, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=500
    )

    for r in rvs:
        all_reviews.append({
            "review": r.get("content"),
            "rating": r.get("score"),
            "date": r.get("at"),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw/bank_reviews_raw.csv", index=False)
print("Scraping completed!")
