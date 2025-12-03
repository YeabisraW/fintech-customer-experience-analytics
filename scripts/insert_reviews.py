import pandas as pd
import psycopg2
from psycopg2 import sql

# Load CSV with UTF-8 encoding
df = pd.read_csv("data/cleaned/bank_reviews_sentiment.csv", encoding="utf-8")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="bank_reviews",
    user="postgres",
    password="postgres"  # replace with your actual password
)
cur = conn.cursor()

# Ensure banks are unique in the table
cur.execute("""
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) UNIQUE,
    app_name VARCHAR(255)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    source VARCHAR(255)
);
""")
conn.commit()

# Insert unique banks only
bank_id_map = {}
for bank in df["bank"].unique():
    cur.execute("""
        INSERT INTO banks (bank_name)
        VALUES (%s)
        ON CONFLICT (bank_name) DO NOTHING
        RETURNING bank_id;
    """, (bank,))
    result = cur.fetchone()
    if result:
        bank_id_map[bank] = result[0]
    else:
        # Bank already exists, fetch its bank_id
        cur.execute("SELECT bank_id FROM banks WHERE bank_name=%s;", (bank,))
        bank_id_map[bank] = cur.fetchone()[0]

conn.commit()

# Insert reviews
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (
            bank_id, review_text, rating, review_date,
            sentiment_label, sentiment_score, source
        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        bank_id_map[row["bank"]],
        row["review"],
        row["rating"],
        row["date"],
        row.get("sentiment_label", None),  # in case missing
        row.get("sentiment_score", None),  # in case missing
        row["source"]
    ))

conn.commit()
cur.close()
conn.close()

print("All reviews inserted successfully with sentiment and UTF-8 handled!")
