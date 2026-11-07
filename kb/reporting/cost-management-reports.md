---
title: "xtraCHEF: Get Started With Cost Management Reports"
source: https://intercom.help/toast-central/en/articles/14728188-xtrachef-get-started-with-cost-management-reports
last_updated: 2026-09-16
area: reporting
---
## What it is (2-4 sentences)
The first section of the **Reporting** page: reports for controlling purchase costs — contracted price variance, COGS, operating summary, price fluctuation between locations, price tracker, purchased items, vendor price comparison and vendor order report. Changes as of Dec 2024: added COGS, Operating summary, Price tracker, Purchased items, Vendor price comparison; removed Food cost ratio and Top 100 product purchase.

## When you'd use it
- Holding vendors to contract pricing, finding cheapest vendor per item, listing all purchases for negotiations.

## How to do it (numbered steps with exact menu paths, button and field names)
**Reporting** in nav → first section. **Star icon** saves to **Favorites** (left).
1. **Contracted Price Variance** — needs contracted prices set (Item Review). Pick **date range** → **Submit**. Columns: location, vendor, invoice date, item code/description, contract price, final purchase price, change $ and %. Drops below contract also show.
2. **Cost of Goods Sold (COGS)** — needs accounting periods, COGS mapping, inventory values (see COGS Report note).
3. **Operating Summary** — also its own nav tab.
4. **Price Fluctuation Comparison** — date range → **Submit**; columns vendor, item, delivered locations (alphabetical), date; **Possible Savings** tab shows $ difference between locations.
5. **Price Tracker** — optional filters Period 1, comparison Period 2, location, vendor, category; updates instantly.
6. **Purchased Items** — **location**, **date range (max 90 days)**, **grouping criteria** → **Submit**.
7. **Vendor Price Comparison** — **location**, **product**, **duration** → **Generate Report**; views **View by Unit Cost** and **View by Price Fluctuation**.
8. **Vendor Order Report** — only orders placed via xtraCHEF Ordering/Order Guides/Purchase Orders; uploaded invoices do NOT appear (use Purchasing by Category, Item Price History, Invoice Summary instead). Empty if nothing matches filters.

## Settings, options & permissions (which roles can do it)
- Not stated here; see User Roles article.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Purchased Items capped at 90 days per run.
- Vendor Price Comparison compares by product — products must group equivalent invoice items from different vendors.

## Automation / efficiency angles
- Weekly: Vendor Price Comparison (View by Unit Cost) for the PFG vs Sysco overlap items.
- Quarterly: Purchased Items (90 days, grouped by vendor) as the data pack for vendor negotiations.
- Set contract prices on key items (e.g., malt, hops contracts, fryer oil) so Contracted Price Variance becomes an automatic overcharge detector — use it to request credits.

## Related articles (links)
- [xtraCHEF: Get Started With Actual vs. Theoretical Analysis Reports](https://intercom.help/toast-central/en/articles/9309126-xtrachef-get-started-with-actual-vs-theoretical-analysis-reports)
- [xtraCHEF: Get Started With User Roles](https://intercom.help/toast-central/en/articles/13730305-xtrachef-get-started-with-user-roles)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF: Get Started With the Price Tracker](https://intercom.help/toast-central/en/articles/14727583-xtrachef-get-started-with-the-price-tracker)
- [xtraCHEF: COGS Report](https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report)
- [xtraCHEF: Item Review](https://central.toasttab.com/s/article/xtraCHEF-Item-Review)
