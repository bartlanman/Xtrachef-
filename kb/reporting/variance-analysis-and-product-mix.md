---
title: "xtraCHEF: Variance Analysis and Product Mix Reports"
source: https://intercom.help/toast-central/en/articles/14727540-xtrachef-variance-analysis-and-product-mix-reports
last_updated: 2026-07-09
area: reporting
---
## What it is (2-4 sentences)
Two recipe reports under **Recipe**: **Variance Analysis** tracks how recipe/prep-recipe ingredient costs change over time from scanned invoices; **Product Mix Report (PMIX)** combines Toast sales with plate costs to show sales, discounts and margins by menu item and by modifier. Both generate automatically once recipes and product mix mapping exist.

## When you'd use it
- Justifying menu price increases; finding low-margin items; seeing how discounts and modifiers erode margin.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereqs**: Recipes and Prep Recipes built; **Product Mix Mapping** done.
1. Nav bar **Recipe** → **Variance Analysis** or **Product Mix Report**.

**Variance Analysis**
1. All recipes listed; filter on the left.
2. **View Details** → plate cost, profit margin, line graph of each ingredient's price over time.
3. Click a blue-highlighted date to see which ingredients moved cost.

**Product Mix Report**
1. Tabs **By Menu Item** / **By Modifier**; date range + calendar icon.
2. **>** carat on an item → data by date; on a modifier → items using it.
- Sales columns: **Menu Price** (from Toast), **Qty Sold**, **Gross Amount** = Price × Qty, **Discounts**, **Net Sales** = Gross − Discounts, **Net Menu Price** = Net Sales ÷ Qty.
- Cost columns: **Gross Margin** (no discounts), **Net Margin** (with discounts), **Prime Cost** (recipe cost of sale).

**Modifiers & prime cost** (only if mapped in xtraCHEF): base = recipe plate cost; add-on modifiers mapped to a product/prep recipe with quantity add cost; removal modifiers (e.g., "No Cheese") subtract if **Subtract** is enabled in Modifier Mapping; nested/size modifiers can be configured. Example: Burger $6.00; +Bacon ($1.25) = $7.25; No Cheese ($0.50, Subtract) = $5.50.

## Settings, options & permissions (which roles can do it)
- xtraCHEF Pro (Recipe module).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- **PMIX is not retroactive** — only populates from the date Product Mix Mapping is complete. Map ASAP.
- Unmapped modifiers don't affect prime cost.

## Automation / efficiency angles
- For a taproom, build pour-size recipes (e.g., 16oz, 10oz, flight taster) mapped to Toast size modifiers so beer margins by style show up in PMIX.
- Monthly: sort By Menu Item by Net Margin ascending; review bottom 10 for price/portion changes.
- Next step: inventory counts unlock Actual vs Theoretical.

## Related articles (links)
- [xtraCHEF: Recipe - Product Mix Mapping](https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping)
- [xtraCHEF: Get Started With Recipes](https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes)
- [xtraCHEF: Sync With Toast Web](https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF: Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
