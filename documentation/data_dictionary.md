# Data Dictionary — Superstore_cleaned.csv

| Column | Type | Description | Notes |
|---|---|---|---|
| Row ID | integer | Sequential row identifier | Unique per row |
| Order ID | string | Order-level identifier | One order can contain multiple line items (rows) |
| Order Date | date (YYYY-MM-DD) | Date the order was placed | See caveat below |
| Ship Date | date (YYYY-MM-DD) | Date the order was shipped | Always ≥ Order Date (verified) |
| Ship Mode | string | Shipping method | Values: Standard Class, Second Class, First Class, Same Day |
| Customer ID | string | Unique customer identifier | Maps 1:1 with Customer Name (verified) |
| Customer Name | string | Customer's full name | |
| Segment | string | Customer segment | Values: Consumer, Corporate, Home Office |
| Country | string | Country of the order | Always "United States" in this dataset |
| City | string | Ship-to city | |
| State | string | Ship-to state | |
| Postal Code | integer | Ship-to ZIP code | |
| Region | string | Sales region | Values: East, West, Central, South |
| Product ID | string | Product identifier | ⚠ 32 IDs map to more than one Product Name — see Insights doc |
| Category | string | Top-level product category | Values: Furniture, Office Supplies, Technology |
| Sub-Category | string | Product sub-category | 17 distinct values |
| Product Name | string | Full product description | |
| Sales | float | Revenue for the line item (USD) | |
| Quantity | integer | Units sold | |
| Discount | float | Discount applied, as a decimal (0.2 = 20%) | Range 0–0.8 |
| Profit | float | Profit for the line item (USD) | Can be negative |

## Known caveat: Order Date

`Order Date` increases by exactly one calendar day for every subsequent row
(2016-08-11 → 2043-12-21). This is almost certainly a synthetic/placeholder
date field rather than genuine order timestamps, and does not reflect real
seasonality. Any month-over-month or seasonal trend read from this column
should be treated as illustrative of the dashboard's capability, not as a
real business finding, until validated against a source with authentic dates.
