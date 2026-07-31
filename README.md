# Superstore Sales & Profitability Analysis

An end-to-end data analysis project on the classic "Sample Superstore" retail
dataset: data cleaning, quality checks, exploratory analysis, and an
interactive HTML dashboard — no server or paid BI tool required.

**Live demo (GitHub Pages — see below):**
(https://byte-forger.github.io/sales_store_analysis/)

## What's in this repo

```
├── data/
│   ├── raw/                      Original, untouched source file
│   │   └── Sample_-_Superstore.csv
│   └── cleaned/                  Cleaned, analysis-ready dataset
│       └── Superstore_cleaned.csv
├── docs/                         ← GitHub Pages site (published live)
│   ├── index.html                Landing page
│   ├── dashboard.html            Interactive KPI + chart dashboard
│   └── data.html                 Themed, searchable data viewer
├── notebooks/
│   └── cleaning_and_analysis.py       Script used to clean data & generate insights
├── documentation/
│   ├── data_dictionary.md        Column-by-column reference
│   └── insights.md               Key findings & recommendations
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Quick start (local viewing)

No installation needed to view the results locally:

1. Open `docs/index.html` in any browser — this is the landing page.
2. From there, click through to the dashboard or the data explorer.

To reproduce the cleaning/analysis:

```bash
pip install -r requirements.txt
python notebooks/cleaning_and_analysis.py
```

## Data source

[Sample - Superstore]([https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final))
is a widely used sample retail dataset (orders, customers, products, sales,
profit) commonly used for BI/analytics practice. **Note:** in this particular
copy of the file, `Order Date` increments by exactly one day per row from
2016-08-11 through 2043-12-21 — this is a data-generation artifact, not real
chronological order data. Any time-based trends should be read with that in
mind (see `documentation/insights.md` for details).

## Data cleaning performed

- Whitespace trimmed from all text fields
- Checked for full-row and Row-ID duplicates (none found — original file was already unique)
- Parsed and standardized `Order Date` / `Ship Date` to ISO format
- Verified no missing/null values in any column
- Verified `Ship Date` is never earlier than `Order Date`
- Flagged (not removed) 32 Product IDs that map to more than one Product Name — a source-data inconsistency worth resolving with the business owner before using Product ID as a join key

See `documentation/insights.md` for the full write-up, including profitability,
discounting, and customer-concentration findings.

## Dashboard features

- KPI cards: total sales, profit, margin, units, discount, orders, customers
- Charts: monthly sales/profit trend, sales by category, profit by region, top 10 sub-categories, discount-vs-profit scatter
- Filters: region, category, segment, ship mode, date range — all charts and the table update live
- Searchable, sortable, paginated order table with CSV export

## License

MIT — see `LICENSE`.
