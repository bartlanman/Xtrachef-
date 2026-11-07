---
title: "xtraCHEF: Map Invoice Items"
source: https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items
last_updated: 2026-07-02
area: invoicing
---

## What it is
**Map invoice items** is the last step of reconciliation and the foundation of all xtraCHEF data. Every invoice line that xtraCHEF hasn't seen before must be assigned a purchase **Category**. Each category maps to a **GL code** synced from the accounting system. After the first mapping, xtraCHEF remembers it and maps that item automatically on future invoices. Mapping drives the accounting extract, purchase totals by GL, category, and item, and food cost tracking.

## When you'd use it
- Whenever the red notification dot appears on **Map invoice items** in the nav bar.
- On every new vendor's first invoices, and whenever a vendor adds new SKUs.
- To merge duplicate items, or to switch an invoice between line-item detail and summary.

## How to do it
**Map items**
1. Click **Map invoice items** in the xtraCHEF nav bar.
2. Open the **Category** drop-down and pick a custom or default category. You can set one for the whole invoice or set each line separately.
3. Repeat until every item is mapped.
4. Select the mapped items and click **Submit Selected Items**.

**Merge duplicate products**
1. On **Map invoice items**, open the row's three-dot overflow menu and choose **Mark as duplicate**.
2. xtraCHEF suggests matches using a distance algorithm. Only products from the same vendor are offered. If the duplicate is caused by a duplicate vendor, contact Customer Care.
3. To override the suggestions, type in **Search**. Wildcard search works on **Item Code** and **Item Description**.
4. Pick the original product and review its properties.
5. Confirm. **The merge can't be undone.**
6. If the original already has a category, the item leaves the queue. If not, it stays in the queue to be categorized.

**Reprocess as Detail or Summary**
- **Purchase Detail**: every line item is read separately. Needed for line-item reporting, inventory, and recipes.
- **Purchase Summary**: one total, with no line detail. xtraCHEF uses this automatically for documents it decides aren't food or beverage.
1. Click the three-dot icon in the **Action** column.
2. Choose **Reprocess Invoice as...**, then **Purchase Detail** or **Purchase Summary**.
3. Click **Reprocess**.

**Fix a wrong category later**: go to **Item library**, search for the item, open it, change the product, category, or GL code (through the category), and click **Save Changes**.

## Settings, options & permissions
- Categories are created in xtraCHEF (custom categories). GL codes are synced from the accounting system.
- Accounts *without* an accounting integration start with **20 default categories** and **predictive mapping**: reviewed documents get a suggested default category that waits for you to review and submit.
- A vendor's **extract preference** (Purchase Summary or Detail) is set on the **Vendors** page.
- The article doesn't name role restrictions.

## Rules, limits & gotchas
- Documents with never-before-seen items, or from new vendors, **stop until they're mapped**. This is the most common reason bills aren't reaching QBO.
- **Submit, not Reprocess.** If invoices keep coming back after you pick a category, you probably clicked Reprocess, which sends the invoice back into processing.
- If invoices from a vendor always arrive as Purchase Summary, check that vendor's extract preference.
- Merging only works within the same vendor, and it's permanent.
- Keep categories detailed (produce, meat, dairy, hops, malt, kegs) while letting several of them roll up to one GL code (for example, Food COGS). You get detailed insight without cluttering the QBO chart of accounts.

## Automation / efficiency angles
- Map at the **invoice level** for single-category vendors (for example, a linen service or a CO2 supplier) to clear them in one click.
- Use **Purchase Summary** as the extract preference for non-inventory vendors (utilities, repairs, cleaning) to cut mapping work. Keep food, beverage, and brewing ingredient vendors on **Purchase Detail** so recipes and inventory get line-level costs.
- Clear the queue daily. Every unmapped item holds back the whole invoice, its extract, and its COGS.
- Merge duplicates as soon as you see them, so price history and recipe costs stay on one item.

## Related articles
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Levels of Reporting](https://intercom.help/toast-central/en/articles/9307954-xtrachef-levels-of-reporting)
- [Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- Custom Categories: https://central.toasttab.com/s/article/xtraCHEF-Custom-Categories
- Vendors (extract preference): https://central.toasttab.com/s/article/xtraCHEF-Vendor-Hub#Extractpreference
- Video: https://play.vidyard.com/UjgrFfhDfsMzhBhnerSZ9Y
