"""
Superstore — Data Cleaning & Analysis
======================================
Reproduces the cleaning steps and the findings in docs/insights.md.

Usage:
    pip install -r requirements.txt
    python notebooks/cleaning_and_analysis.py
"""
import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).parent.parent / "data" / "raw" / "Sample_-_Superstore.csv"
CLEAN_PATH = Path(__file__).parent.parent / "data" / "cleaned" / "Superstore_cleaned.csv"


def load_and_clean(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin1")

    # Trim whitespace on every text column
    str_cols = df.select_dtypes(include="object").columns
    for c in str_cols:
        df[c] = df[c].astype(str).str.strip()

    # Drop exact duplicate rows (none expected, but safe to keep this step)
    before = len(df)
    df = df.drop_duplicates()
    print(f"Duplicates removed: {before - len(df)}")

    # Standardize dates
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d %B %Y", errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d %B %Y", errors="coerce")

    return df


def quality_checks(df: pd.DataFrame) -> None:
    print("\n--- Data quality checks ---")
    null_counts = df.isnull().sum()
    nonzero = null_counts[null_counts > 0]
    print("Nulls per column:\n", nonzero if not nonzero.empty else "None")
    print("Ship Date < Order Date violations:", (df["Ship Date"] < df["Order Date"]).sum())

    dupe_ids = df.groupby("Product ID")["Product Name"].nunique()
    print("Product IDs mapping to >1 Product Name:", (dupe_ids > 1).sum())

    cust_ids = df.groupby("Customer ID")["Customer Name"].nunique()
    print("Customer IDs mapping to >1 Customer Name:", (cust_ids > 1).sum())


def key_insights(df: pd.DataFrame) -> None:
    print("\n--- Key insights ---")
    print("Total Sales:", round(df["Sales"].sum(), 2))
    print("Total Profit:", round(df["Profit"].sum(), 2))
    print("Orders:", df["Order ID"].nunique(), " Customers:", df["Customer Name"].nunique())

    neg = df[df["Profit"] < 0]
    print(f"Loss-making line items: {len(neg)} ({len(neg)/len(df):.1%}), total loss {neg['Profit'].sum():.2f}")

    print("Discount vs Profit correlation:", round(df["Discount"].corr(df["Profit"]), 3))

    bucket = pd.cut(df["Discount"], bins=[-0.01, 0, 0.2, 0.4, 1], labels=["0%", "1-20%", "21-40%", "40%+"])
    print("\nProfit by discount bucket:\n", df.groupby(bucket, observed=True)["Profit"].sum())

    cust_sales = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)
    cum_share = cust_sales.cumsum() / cust_sales.sum()
    n80 = (cum_share <= 0.8).sum()
    print(f"\nCustomers driving 80% of sales: {n80} of {len(cust_sales)} ({n80/len(cust_sales):.1%})")


if __name__ == "__main__":
    df = load_and_clean(RAW_PATH)
    quality_checks(df)
    key_insights(df)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"\nCleaned file written to {CLEAN_PATH}")
