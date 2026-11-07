---
title: "xtraCHEF: Get Started With the Item Library"
source: https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library
last_updated: 2026-09-01 (date shown on article)
area: inventory
---
## What it is
The Item Library is the master list of every invoice line item xtraCHEF has ever read, plus the **Products** those items roll up into. It fills in on its own as invoices are uploaded. Each item's unit setup (Purchase unit / Pack / Size / Unit / Inventory unit) decides how case costs get broken into per-bottle, per-liter, per-pound and similar costs. Every recipe cost, inventory value and food-cost report depends on that breakdown.

## When you'd use it
- To review and approve new items flagged **To Review** after invoices process.
- To fix a wrong unit breakdown, for example when a keg or case cost per ounce looks wrong in a recipe.
- To assign items to Products (ingredients) and Categories (which set the GL code).
- To bulk re-categorize items, check the last purchase price, or export everything to a spreadsheet.

## How to do it
**Reviewing new items**
1. Open **Item Library** from the xtraCHEF nav bar.
2. Items still waiting for review sit at the top with status **To Review**. To isolate them, go to **More Filters** → **To Review** → **Apply filters**.
3. Click the item name (it's a hyperlink) to open the detail view.
4. Click the yellow **"Item seen on: Row X"** highlight to jump to that line on the source invoice.
5. Check **Purchase unit**, **Pack**, **Size**, **Unit** and **Inventory unit**.
6. Read the sentence xtraCHEF builds in the blue box at the bottom. If it doesn't describe how the item actually ships, fix the unit fields.
7. Optionally set **Product** and **Category**. Category drives the **GL code**.
8. Click **Approve**.

**Editing an approved item**
1. Click the item in the Item Library. If it's still To Review, go through the review steps first.
2. Scroll to the **Line Item Details** tile. You can edit Purchase unit, Pack, Size, Unit, Inventory unit (where it applies), Product and Category. Typing a new name in **Product** creates that product.
3. Confirm with the blue "Check your work: does this sentence make sense?" box.

**Products view**
1. Click **View products** at the top of the Item Library.
2. Click a product name to see the invoice items linked to it. In **Edit product** you can change Product Name, **Yield**, **Unit** and the **Density Calculator** conversion (at the bottom of the sidebar). You can also edit the invoice unit fields (Purchase unit, Pack, Size, **Size unit**, Inventory unit). Click **Save changes** when done.
3. **Delete product** removes the whole product. The **blue minus icon** next to an invoice item unlinks just that item.
4. The three-dot menu on a product row offers **View last invoice**, **Rename product** and **Product details**. Product details shows the linked invoice items, recipes and count lists, which is handy before you delete or merge anything.

**Other tools on the page**
- Filters: **Location**, **Category**, **Product**, **Vendors**. **More Filters** adds **Status** and **Last Purchase Date**.
- Search for a product to see every linked invoice item across all locations (unless a filter is narrowing it).
- **Download all** builds a spreadsheet in the background, and you get a notification when it's ready.
- Bulk categorize: tick the item checkboxes, then click **Categorize**.
- The columns now include **Last Purchased** and **Most Recent Price**.

## Settings, options & permissions
- The article doesn't name roles. Role access is covered in "xtraCHEF: Access to Inventory Features by Role" (kb/admin-and-users).
- Categories in the dropdown come from the synced Chart of Accounts (QuickBooks) or from GL codes and categories created in xtraCHEF.

## Rules, limits & gotchas
- **Field definitions:**
  - Purchase unit = the unit shown on the invoice.
  - Pack = how many measurable units are in the case. Defaults to 1.
  - Size = the quantity in each pack.
  - Unit = the unit of measure for Size.
  - Inventory unit = the name for one pack. It only applies when Pack > 1, and defaults to "each" if left blank.
- **Liquor:** set it up by the **liter**, not fl oz or ml, so reporting stays consistent. A case of 12 × 1 L is Case / 12 / 1 / Liter / Bottle. A single bottle is Bottle / 1 / 1 / Liter / N/A.
- **Wine:** set it up by **each**, not by volume. A case of 12 is Case / 12 / 1 / Each / Bottle. A single bottle is Bottle / 1 / 1 / Each / N/A.
- **Kegs** (Purchase unit Keg, Pack 1, Unit Gal, Inventory unit Keg):
  - 1/2 bbl = Size 15.5 gal
  - 1/4 bbl = Size 7.75 gal
  - 1/6 bbl = Size 5.2 gal
- **Cans and bottles by the case:** Case / pack count / Size 1 / Each / Can (or Bottle). Example: a 6-can case is Case / 6 / 1 / Each / Can.
- **Same product, two valid setups:** a 10 lb case of apples can be Case/10/1/Lb/Lb or Case/1/10/Lb/N/A. A 5 lb bag of sugar can be Bag/5/1/Lb/Lb or Bag/1/5/Lb/N/A. Pick whichever matches how you count it.
- Changing **Category** changes the **GL code**, and that changes how the line exports to QuickBooks.
- A blank Category can mean the item is still sitting in **Map invoice items**.
- Products are what recipes and count lists use. Linking substitute items (a different brand or vendor for the same ingredient) to one product keeps plate cost and inventory value correct when you switch suppliers.
- The protein video covers three setups: by the pound (used by weight), by case/pack used by weight, and by case/pack used by each.

## Automation / efficiency angles
- **Brewery keg standard:** set every purchased (guest) keg as Keg/1/15.5 (or 7.75, 5.2)/Gal/Keg. xtraCHEF then works out cost per gallon, so a pour recipe in fl oz costs correctly. House beer moved from the brewery to the taproom can be handled the same way if it's invoiced or tracked as a product.
- Do a weekly **To Review** sweep with the filter (More Filters → To Review). An agent can pull this list and flag items whose blue-box sentence implies an impossible price, such as a $0.02 keg.
- Use **Download all** and diff against last week's export to catch price jumps (Most Recent Price vs earlier). This pairs well with the PFG vs Sysco price-check skill.
- Bulk **Categorize** new items by vendor (filter Vendors → select all → Categorize) so the QuickBooks GL coding stays consistent.
- Check **Product details** before deleting a product so you don't break recipes or count lists.

## Related articles
- Get Started With Products: https://intercom.help/toast-central/en/articles/9303010-xtrachef-get-started-with-products
- Create Products: https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products
- Product Verification: https://intercom.help/toast-central/en/articles/14727562-xtrachef-product-verification
- Assign Invoice Items to Products: https://intercom.help/toast-central/en/articles/14727680-xtrachef-assign-invoice-items-to-products
- Glossary and Terminology: https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology
- Custom Categories: https://central.toasttab.com/s/article/xtraCHEF-Custom-Categories
- Recipe Yield and Density Calculator: https://intercom.help/toast-central/en/articles/14727732-xtrachef-recipe-yield-and-density-calculator
- Videos: overview https://play.vidyard.com/PZQ4gBvEkri1runijJ9sdf · protein https://play.vidyard.com/ZaTr4KWkjnmtPaaN38BEV6 · on-demand https://share.vidyard.com/watch/EEutzGtwVbrnAEnzLjsghL
