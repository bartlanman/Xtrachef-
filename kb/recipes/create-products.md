---
title: "xtraCHEF: Create Products"
source: https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products
last_updated: 2026-04-28 (date shown on article)
area: recipes
---
## What it is
Products are the ingredients and inventory items that recipes and count lists are built from. Several invoice items (different vendors, brands or pack sizes of the same thing) roll up into one product. This article covers creating products manually or by bulk import in the Item Library.

## When you'd use it
- During setup, to create the ingredient list before building recipes or count lists, ideally all at once from a spreadsheet.
- To add a few products later, for example for a new menu item or a new guest beer.

## How to do it
**Bulk import**
1. Go to **Item library > View products > + Add products > Import file**, then click **Download template** (lower left of the pop-up).
2. In the template's **Fill This Out** tab, list names in the **Product** column and set a **Purchase Unit** of **Weight**, **Volume** or **Each** for each.
3. Save it as .xlsx or .csv, then use **+ Browse Files** or drag and drop. Your own file works if the columns match.
4. Click **Import**, wait, then click **Add Products**.
5. Confirm with **Yes, save**. A message shows how many were added, and **Undo** on that message reverses the whole import.
6. Errors appear under **Invalid** (upper right). The usual causes are special characters in the name, or a Purchase Unit other than Weight, Volume or Each. Fix them on screen, or fix the file and use **Re-import file**.

**Manual**
1. Go to **Item library > View products > + Add Products**.
2. Enter a name and choose a purchase unit. Click **+ Add Product** for more rows.
3. Click **Add Products** (upper right).

## Settings, options & permissions
- No roles are stated in the article.

## Rules, limits & gotchas
- A product's unit family is only **Weight**, **Volume** or **Each**. Choose it based on how the product is *used* in recipes and counts. Kegs and spirits are Volume, wine is Each (per the Item Library guidance), proteins are usually Weight.
- Special characters in names are rejected. The article doesn't list which ones, so stick to letters, numbers and spaces.
- After creating products, map invoice items to them (Map Invoice Items / Assign Invoice Items to Products). An unlinked product has no cost.
- To change a product's unit family later, see "Reassign Product Unit for Products and Associated Items."

## Automation / efficiency angles
- An agent can produce the import file from the Item Library **Download all** export plus the Toast menu: one row per ingredient with its unit family, for example "Guest Keg – [Beer Name]" as Volume, "Chicken Wings" as Weight, "Burger Bun" as Each.
- Use a consistent naming pattern (category prefix plus item: "Keg – IPA – Guest", "Liquor – Bourbon – Well") so products sort neatly in count lists and drop-downs.
- **Undo** on the confirmation message makes a test import cheap. Try a small batch first.

## Related articles
- Get Started With Products: https://intercom.help/toast-central/en/articles/9303010-xtrachef-get-started-with-products
- Get Started With the Item Library: https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library
- Product Verification: https://intercom.help/toast-central/en/articles/14727562-xtrachef-product-verification
- Assign Invoice Items to Products: https://intercom.help/toast-central/en/articles/14727680-xtrachef-assign-invoice-items-to-products
- Reassign Product Unit: https://intercom.help/toast-central/en/articles/14726299-xtrachef-reassign-product-unit-for-products-and-associated-items
- Create Orders on Mobile: https://intercom.help/toast-central/en/articles/14727628-xtrachef-create-orders-on-mobile
- Video: https://play.vidyard.com/TcJRwssMxL2no1bWxshgnB
