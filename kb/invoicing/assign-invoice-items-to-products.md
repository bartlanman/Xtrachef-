---
title: "xtraCHEF: Assign Invoice Items to Products"
source: https://intercom.help/toast-central/en/articles/14727680-xtrachef-assign-invoice-items-to-products
last_updated: 2026-04-22
area: invoicing
---

## What it is
Every invoice line becomes an "invoice item" in the **Item Library**. A single invoice item is just one SKU or pack from one vendor. A **product** groups several invoice items (different brands, pack sizes, containers, vendors) into one logical ingredient or inventory item. Assigning items to products is what keeps recipe costing and inventory accurate when purchasing changes.

## When you'd use it
- During item review, right after new invoices are parsed.
- When you switch brands or pack sizes. For example, a new case size of chicken breast or a different hop supplier's pellet bag should roll up under the same product.
- Periodic cleanup of invoice items that were approved but never linked to a product.

## How to do it
**Normal path: during item review**
1. Click **Item library** in the xtraCHEF navigation bar.
2. In item review, verify each new line item and assign it to a product as you approve it.

**Cleanup path: approved items without a product**
1. In Item Library, open the **Product** filter drop-down and choose **Unassigned**.
2. For each item, fill in the **Product** field with an existing product.
3. To make a new product, type its name in the **Product** field and click **+ Add**.
4. Click **Approve**.

## Settings, options & permissions
- The article lists no specific role requirement. Users need Item Library access.
- Prerequisite: the invoice must already be uploaded, parsed, and cataloged.

## Rules, limits & gotchas
- Items that aren't linked to a product won't flow cleanly into recipes or inventory, so prices for a "new" SKU look missing.
- Item review is the main defense against bad data skewing recipe and inventory reports. Don't skip it.
- Each new brand, size, or pack shows up as a new invoice item, even from the same vendor.

## Automation / efficiency angles
- Make **Product = Unassigned** a weekly saved check. It should trend to zero.
- Settle on a product naming convention (for example, "Chicken Breast, boneless") before building, so new items map quickly with type-ahead.
- When onboarding a new vendor, such as moving from PFG to Sysco, map all of their SKUs in one session to existing products so recipe costs carry over.

## Related articles
- [Get Started With Products](https://intercom.help/toast-central/en/articles/9303010-xtrachef-get-started-with-products)
- [Get Started With the Item Library](https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library)
- [Create Products](https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Reassign Product Unit](https://intercom.help/toast-central/en/articles/14726299-xtrachef-reassign-product-unit-for-products-and-associated-items)
- [xtraCHEF 101](https://intercom.help/toast-central/en/articles/14727601-xtrachef-101)
