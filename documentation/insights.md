# Key Insights — Superstore Analysis

## 1. Headline numbers
- Total Sales: **$2,297,200.86**
- Total Profit: **$286,397.02** (12.5% overall margin)
- Orders: **5,009** across **793** customers
- Average discount applied: **15.6%**

## 2. Data quality findings
- No missing values, no full-row duplicates, no whitespace issues in the source file.
- `Ship Date` is never earlier than `Order Date` (0 violations) — shipping logic is internally consistent.
- **32 Product IDs map to more than one Product Name** (e.g. `FUR-BO-10002213` is used for both a bookcase and a completely different library unit). This is a real data-quality issue: don't join or group by Product ID alone without resolving these first.
- 1,167 line items (~11.7%) are statistical outliers on Sales (IQR method, upper bound ≈ $499) — mostly large bulk/enterprise orders rather than errors, but worth a manual spot-check before using Sales in any model sensitive to outliers.
- `Order Date` is synthetic (see data dictionary) — don't draw seasonality conclusions from it without a caveat.

## 3. Profitability
- **1,871 line items (18.7% of all rows) lose money**, totaling **–$156,131** in losses.
- Discount and Profit are **negatively correlated (r ≈ –0.22)** — heavier discounting is associated with lower profit.
- Discount-bucket breakdown makes this concrete:

  | Discount Range | Total Profit | Avg Profit/Order |
  |---|---|---|
  | 0% | $320,988 | $66.90 |
  | 1–20% | $100,785 | $26.50 |
  | 21–40% | –$35,817 | –$77.86 |
  | 40%+ | –$99,559 | –$106.71 |

  **Every discount above 20% is net destructive to profit on average.**

- Least profitable sub-categories: **Tables (–$17,725)** and **Bookcases (–$3,473)** — both also carry above-average discount rates (26% and 21% respectively), reinforcing the discount-profit link.
- Most profitable sub-categories: **Copiers ($55,618)**, **Phones ($44,516)**, **Accessories ($41,937)**.

## 4. Customer concentration
- **395 customers (49.8% of the customer base) generate 80% of total sales.** Revenue is broadly distributed rather than concentrated in a tiny VIP tier — a classic 80/20 rule does *not* strictly apply here, which has implications for account-based retention strategy (it's not just about a handful of whales).

## 5. Shipping mode vs. margin
| Ship Mode | Sales | Margin % |
|---|---|---|
| First Class | $351,428 | 13.93% |
| Second Class | $459,194 | 12.51% |
| Same Day | $128,363 | 12.38% |
| Standard Class | $1,358,216 | 12.08% |

First Class orders actually carry the *highest* margin, not the lowest — faster shipping is not eating into profitability here, which is a useful, slightly counterintuitive finding to highlight.

## 6. Recommendations
1. **Cap discounts at 20%** on Tables and Bookcases specifically, or renegotiate cost basis — these two sub-categories are actively losing money and are the main drag on Furniture-category profit.
2. **Investigate the 32 duplicate-mapped Product IDs** with whoever owns the source system before this data is used for product-level reporting or joins.
3. **Don't chase a small VIP segment** — with sales spread across ~half the customer base, broad retention/loyalty programs likely outperform narrow VIP-only ones.
4. **Re-validate the Order Date field** with the data source owner before presenting any time-trend chart externally — it currently increments by exactly one day per row.
5. Treat the ~1,167 Sales outliers as a segment worth understanding (bulk/enterprise orders) rather than excluding them by default.
