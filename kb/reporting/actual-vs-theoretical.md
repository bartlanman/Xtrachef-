---
title: "xtraCHEF: Get Started With Actual vs. Theoretical Analysis Reports"
source: https://intercom.help/toast-central/en/articles/9309126-xtrachef-get-started-with-actual-vs-theoretical-analysis-reports
last_updated: 2026-08-25
area: reporting
---
## What it is (2-4 sentences)
The **Actual vs. Theoretical (AVT)** report compares what you actually used (from physical counts and purchases) with what Toast sales say you should have used (from recipes). The gap — variance — points to waste, theft, over-portioning, unrung sales or count errors. It is one of two Inventory Analytics reports (with Depleting Inventory).

## When you'd use it
- After each inventory count to measure shrink; investigating rising COGS.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereqs**: ≥2 physical inventory counts; Product Mix Mapping done. Log waste via **Manage Waste** to keep it accurate.
1. **Reporting** → **Inventory** section → **Actual vs theoretical**.
2. Pick start and end dates (only dates with a submitted count). Opening = From-date count; closing = To-date count.
3. Prompt "How would you prefer to handle purchases and sales in this report?" → **Include purchases and sales numbers from [start date]** or **…from [end date]**.
4. **Submit**.
5. **Cost** / **Quantity** slider.
6. Drill: **Purchase** value → sidebar with vendor, invoice #, qty in invoice and product units. **Theoretical Consumption** value → menu items and qty sold (scroll right). Removal modifiers ("no pickles") show negative theoretical — expected.

**Product Unit Price** column: last purchase price for that product at the selected location; drives all cost values (opening, purchases, closing, waste, actual, theoretical, variance). Stale if not recently bought.

Formulas:
- Actual = Opening + Purchases − Closing (e.g., 50 + 100 − 60 = 90 avocados).
- Theoretical = recipe qty × items sold, summed over menu items (1 × 100 toasts = 100; at $1 = $100).
- Variance = Actual − Theoretical (90 − 100).

## Settings, options & permissions (which roles can do it)
- xtraCHEF Pro (Inventory).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Theoretical data lags **2–3 business days** after the range end — don't run it the morning after a count.
- Theoretical errors come from recipes (wrong UOM/measurement, wrong product prices from Item Review/Item Library), prep recipe mapping/batch sizes, or modifier mapping.
- Actual errors come only from counts (wrong quantities, missed products).
- Actual food cost is usually higher than theoretical.

## Automation / efficiency angles
- Count on a fixed cadence (e.g., every Sunday close or period end) and run AVT 3 business days later.
- Track variance % per count in a log to spot trends; top variance $ items get a spot count.
- For draft beer, map pour recipes so keg depletion vs counted kegs reveals overpour/comp leakage.

## Related articles (links)
- [xtraCHEF: Review Inventory Analytics](https://intercom.help/toast-central/en/articles/14727647-xtrachef-review-inventory-analytics)
- [xtraCHEF: Variance Analysis and Product Mix Reports](https://intercom.help/toast-central/en/articles/14727540-xtrachef-variance-analysis-and-product-mix-reports)
- [xtraCHEF: Train on Advanced Inventory](https://intercom.help/toast-central/en/articles/14487654-xtrachef-train-on-advanced-inventory)
- [xtraCHEF: Introduction to Reporting and Analytics](https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics)
- [Toast Inventory: Inventory Variance Reports (Canada, Ireland, and UK)](https://intercom.help/toast-central/en/articles/14022638-toast-inventory-inventory-variance-reports-canada-ireland-and-uk)
