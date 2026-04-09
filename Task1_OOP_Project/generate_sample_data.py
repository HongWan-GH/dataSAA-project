import os
import csv
import random

def create_sample_files():
    folder_name = "monthly_statements"
    os.makedirs(folder_name, exist_ok=True)
    tickers = ["AAPL", "GOOGL", "GOLD", "TSLA", "MSFT"]
    
    for month in range(1, 13):
        days = 28 if month == 2 else 30
        fname = os.path.join(folder_name, f"2026-{month:02d}-statement.csv")
        with open(fname, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(["TICKER", "ACTION", "PRICE", "QUANTITY", "DATE"])
            for _ in range(15):
                t = random.choice(tickers)
                a = random.choice(["BUY", "SELL"])
                p = round({"AAPL": 150, "GOOGL": 140, "GOLD": 2100, "TSLA": 200, "MSFT": 400}[t] * random.uniform(0.9, 1.1), 2)
                q = random.randint(5, 50)
                d = f"2026-{month:02d}-{random.randint(1, days):02d}"
                w.writerow([t, a, p, q, d])
    print(f"Generated 12 monthly sample CSV files in '{os.path.abspath(folder_name)}' directory!")

if __name__ == "__main__":
    create_sample_files()
