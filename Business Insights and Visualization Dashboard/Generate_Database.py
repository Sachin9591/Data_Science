import sqlite3
import pandas as pd
from datetime import datetime
import random

# -------------------------------------------
# Create SQLite Database & Table
# -------------------------------------------

conn = sqlite3.connect("business_data.db")
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS sales_data;
""")

cursor.execute("""
CREATE TABLE sales_data (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    region TEXT
);
""")

conn.commit()

# -------------------------------------------
# Insert Sample Records (Randomly Generated)
# -------------------------------------------

products = [
    ("Laptop", "Electronics"),
    ("Mouse", "Electronics"),
    ("Headphones", "Electronics"),
    ("Chair", "Furniture"),
    ("Desk", "Furniture"),
    ("Pen", "Stationery"),
    ("Notebook", "Stationery"),
]

regions = ["North", "South", "East", "West", "Central"]

sample_rows = []

for i in range(1, 501):  # Generate 500 sales rows
    product, category = random.choice(products)
    quantity = random.randint(1, 10)
    price = round(random.uniform(100, 50000), 2)
    order_date = datetime(2024, random.randint(1,12), random.randint(1,28)).strftime("%Y-%m-%d")
    region = random.choice(regions)

    sample_rows.append((i, random.randint(1000, 9999), order_date, product, category, quantity, price, region))

cursor.executemany("""
INSERT INTO sales_data (order_id, customer_id, order_date, product, category, quantity, price, region)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", sample_rows)

conn.commit()
conn.close()

print("business_data.db created successfully with 500 sample rows!")
