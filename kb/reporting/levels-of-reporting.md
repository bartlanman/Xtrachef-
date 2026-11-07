---
title: "xtraCHEF: Levels of Reporting"
source: https://intercom.help/toast-central/en/articles/9307954-xtrachef-levels-of-reporting
last_updated: 2026-02-01
area: reporting
---
## What it is (2-4 sentences)
Explains xtraCHEF's four-level data hierarchy used by every report: **GL Codes** (broadest) → **Categories** → **Products** → **Invoice Items** (most specific). Reports start at GL and drill down.

## When you'd use it
- Designing your chart of accounts/category structure; understanding why a report groups things the way it does.

## How to do it (numbered steps with exact menu paths, button and field names)
1. **GL Codes** — your chart of accounts (e.g., Food Purchases, Beverage Purchases); usually from your accountant/QBO.
2. **Categories** — xtraCHEF-only sub-layer within a GL (e.g., Food Purchases → Protein, Produce, Seafood). Do **not** change AP automation or accounting extracts; invoices still post to the GL.
3. **Products** — ingredients/inventory items; foundation for Recipes and Inventory; group substitutable invoice items so costs survive vendor swaps.
4. **Invoice Items** — line items/item numbers read from invoices; form the Item Library; mapped to Products in Item Review.

## Settings, options & permissions (which roles can do it)
- N/A (conceptual).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Only the GL level reaches QuickBooks; categories, products and COGS groups are reporting-only.

## Automation / efficiency angles
- Keep QBO GLs broad (Beer Ingredients, Food, NA Beverage, Packaging, Supplies) and do detail in categories — fewer GL mapping errors, richer xtraCHEF reporting.

## Related articles (links)
- [xtraCHEF: Introduction to Reporting and Analytics](https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics)
- [xtraCHEF: Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [xtraCHEF: Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
- [xtraCHEF General Ledger Codes](https://central.toasttab.com/s/article/xtraCHEF-General-Ledger-Codes)
- [xtraCHEF Custom Categories](https://central.toasttab.com/s/article/xtraCHEF-Custom-Categories)
