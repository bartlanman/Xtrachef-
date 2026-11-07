---
title: "xtraCHEF: Get Started With Inventory Area Setup and Count Lists"
source: https://intercom.help/toast-central/en/articles/14728252-xtrachef-get-started-with-inventory-area-setup-and-count-lists
last_updated: 2026-04-22 (date shown on article)
area: count-lists
---
## What it is
Explains the three-part inventory setup: **Area Setup** (physical storage areas and sub areas, count schedule, who counts), **Count Lists** (which products are counted in each area, in what order, with PARs), and **Inventory Counts** (doing the count). Inventory Management and Recipe Costing are **Pro-suite** features only.

## When you'd use it
- At initial inventory setup for each location.
- When adding a new storage space (new walk-in, keg cooler, bar backstock) or changing the count schedule.
- When setting or adjusting PAR levels, including seasonal PARs.

## How to do it
**First area (one location at a time; confirm the location selector at the top first)**
1. Open the **Inventory** tab and click **Setup Inventory**.
2. Choose one or more areas. The defaults are **Walk-In, Freezer, Prep Area, Liquor, Dry Goods, Cooler**. Use **+ Add Custom Area** for anything else. Click **Next**.
3. (Optional) Add **Sub Areas** with the plus symbol, give each a name, and click **Next**.
4. **Schedule.** The default is 12 am daily. Choose **Daily**, **Weekly**, **Monthly** or **Accounting cycle** and fine-tune it in the **Schedule** section. **Adhoc** lets you pick any day of the month and decide whether it repeats. Click **Save Schedule**.
5. **Inventory takers.** Click **+ Assign** and pick specific users or **All Restaurant Managers**, then **Save**.
6. (Optional) **Instructions.** Click **+Add** to leave counting notes for the area.
7. Review and click **Finish** (or **Cancel** to discard).

**More areas:** go to **Inventory > Area Setup** → **+ Add New Area** and follow the same flow (users are added via **+ Create**). Use the **expand icon** on an area to align its schedule and add sub areas.

**Count lists**
1. Go to **Inventory > Count Lists** → **+ Create New** next to the area.
2. Click the default name **New Count List** to rename it.
3. Drag products into the list and into sub areas. **Shift+click** selects several at once. Products, invoice items and prep recipes can all be added.
4. If an item is missing, it isn't assigned to a product yet (see Create Products).
5. Flip the **Unpublished/Published** slider (top right) to Published and confirm. Unpublished lists can't be counted.
6. **Preview.** Go to **Inventory > Count Lists** → **Action** → **Preview List** to see a mock count sheet.

**PAR levels**
1. On the count list, click the **3-dot icon** next to a product → **Inventory Configuration**.
2. Turn on the par level and enter the amount. PAR is set in the item's **purchase unit**.
3. For seasonal PARs, pick a month and set a different amount for it.
4. **Need to Order** appears on the right side of the count list.

## Settings, options & permissions
- Pro suite is required.
- Counters are assigned per area (individual users or All Restaurant Managers).
- Full role details are in "Access to Inventory Features by Role" (https://intercom.help/toast-central/en/articles/14727495-xtrachef-access-to-inventory-features-by-role).

## Rules, limits & gotchas
- **End-of-day rule:** if you count before opening, schedule the count for the **previous business day** so it records before that day's sales and doesn't override depletion.
- PARs are **per count list**. They don't carry over, and the same product can have a different PAR on another list.
- PAR units = purchase unit (cases, kegs and so on).
- Item cost on the list shows the **Last Purchase Price** of the most recent item in the product.
- Each location is set up separately.

## Automation / efficiency angles
- **Shelf-to-sheet order:** make sub areas match the physical layout (Walk-In → Shelf 1 top to bottom; Keg Cooler → by tap line; Bar → Well, Back Bar, Backstock; Dry Storage → by rack) and drag products in walking order. Counts get faster and fewer items get missed.
- Suggested Basic City areas: Walk-In, Freezer, Dry Goods, Prep Area, Keg Cooler (custom), Bar/Liquor, Can/Bottle Cooler (custom), Disposables/Packaging (custom).
- Schedule a weekly count (e.g., Sunday close or Monday early, dated back to Sunday) plus the **Accounting cycle** period-end count so COGS closes cleanly.
- Use seasonal PARs for patio season or summer festivals versus winter.
- Add prep recipes (sauces, dough, batched cocktails) to count lists so the work-in-progress value is captured.

## Related articles
- Inventory Counts: https://intercom.help/toast-central/en/articles/14727473-xtrachef-inventory-counts
- Mobile Inventory: https://intercom.help/toast-central/en/articles/14727545-xtrachef-mobile-inventory
- Get Started With Products: https://intercom.help/toast-central/en/articles/9303010-xtrachef-get-started-with-products
- Get Started With Inventory Reports: https://intercom.help/toast-central/en/articles/9308181-xtrachef-get-started-with-inventory-reports
- Access to Inventory Features by Role: https://intercom.help/toast-central/en/articles/14727495-xtrachef-access-to-inventory-features-by-role
- Expert-led training (Toast Classroom): https://central.toasttab.com/s/article/xtraCHEF-Expert-Led-Training-Sessions#demand
