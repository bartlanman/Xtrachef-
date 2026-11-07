---
title: "xtraCHEF: Change an Invoice Item's GL Code or Category"
source: https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category
last_updated: 2026-09-24
area: invoicing
---

## What it is
After an item has been mapped, xtraCHEF applies the same category, and therefore the same GL code, to every future invoice line for that item. To change it, you edit the item in the **Item library**. You can't edit the GL code directly. It always follows the category you choose.

## When you'd use it
- When an item was mapped to the wrong category (for example, cleaning chemicals coded as food).
- When you restructure categories or GL accounts and need to re-point items.

## How to do it
1. Click **Item library** in the nav bar.
2. Find the item using the search bar and/or filters.
3. Click the item to open its details.
4. Scroll to **Category** and pick the new category. The **GL code** updates automatically. The GL field can't be edited.
5. Click **Save Changes**. The update is saved and published.

Bonus: the **Invoices** page search bar accepts plain-English (LLM) queries, such as "invoices mapped to [category] in the last 60 days" or "invoices for [location] under $X". Use it to find the affected invoices.

## Settings, options & permissions
- This applies only to items that are already mapped to a category.
- Editing a category itself (its name or GL mapping) is covered in the separate "Create and Edit Purchase Categories" article.
- No roles are stated.

## Rules, limits & gotchas
- To change a GL code, change the category, or change the category's GL mapping. There is no per-item GL override field.
- The article doesn't say whether past, already-extracted invoices are re-coded. Assume a QBO bill that has already synced has to be corrected in QBO itself. *(Inference; verify.)*

## Automation / efficiency angles
- Spot-check the Spending by GL analytics every month. A category that jumps unexpectedly usually means a mis-mapped item, which you fix here.
- Use natural-language invoice search to find every invoice touched by the bad mapping in one query, then fix QBO for the invoices that already extracted.

## Related articles
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [General Ledger (GL) Codes](https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes)
- [Invoice Search](https://intercom.help/toast-central/en/articles/14726221-xtrachef-invoice-search)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Get Started With Spending by GL Analytics](https://intercom.help/toast-central/en/articles/14728263-xtrachef-get-started-with-spending-by-gl-analytics)
- Create and Edit Purchase Categories: https://support.toasttab.com/en/article/xtraCHEF-Custom-Categories?lang=en_US
