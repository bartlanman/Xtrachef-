---
title: "xtraCHEF: Mobile Inventory"
source: https://intercom.help/toast-central/en/articles/14727545-xtrachef-mobile-inventory
last_updated: 2026-07-13 (date shown on article)
area: inventory
---
## What it is
The xtraCHEF phone app lets counters walk the building area by area and type in on-hand quantities, instead of using clipboards and keying numbers in afterward. Counts entered on mobile show up in desktop xtraCHEF and feed COGS, Inventory Reports and Inventory Analytics.

## When you'd use it
- For every scheduled count: walk-in, keg cooler, bar wells, dry storage, freezer.
- To add an item that's on the shelf but missing from the count list, mid-count.
- To check a submitted count's summary (value change, below-par items) from your phone.

## How to do it
**Prerequisite:** Inventory Areas and Count Lists must already exist (set up on desktop).

**Count**
1. Tap **Inventory** in the bottom nav.
2. Tap **Start counting** on a count list that's due.
   - If the list isn't showing, a **Tenant Admin** has to unlock it in a web browser by clicking **+ Add Inventory** on that count list.
3. Tap a **Product**.
4. Tap the blank field under the item's UOM and enter the quantity on hand. The UOMs available come from the invoice items grouped under that product during **Item Review**.
5. If there's none on hand, tap **Out of stock** to set the quantity to zero.
6. Tap **Save**.
7. Repeat steps 3–6 for every item.
8. Tap **Submit count**.
9. A **Summary** screen shows what you entered. It's visible on desktop and mobile.

**Review a submitted count**
1. On the Inventory page, tap **View details**.
2. Switch between the inventory details and the summary. The summary shows **Beginning** and **Ending inventory values**, **% change**, and stock buckets: **Below Par**, **Out of Stock**, **In Stock**, **Not counted**.

**Add an item during a count**
1. On the open count, tap **Add item**.
2. Search for and pick the item, then tap **Next**.
3. If the area has sub areas, choose one (or **Unassigned**), then tap **Add item**.
4. A green confirmation appears.

## Settings, options & permissions
- Unlocking or opening a count list that isn't visible needs a **Tenant Admin**, working on desktop.
- The rest of role access is in "Access to Inventory Features by Role."

## Rules, limits & gotchas
- The count units you can pick are whatever the linked invoice items define. If a keg can only be counted in "Keg" and you want partial kegs, fix the item units in the Item Library first (for example, make sure gallons are available).
- **A closed period doesn't roll forward.** If every count was submitted and the period closed, you have to download the prior month's counts yourself and re-enter them in the current month.
- **Fixing a missed count:** pick that specific date, then the count list.
- Counts are end-of-day entries (see Inventory Counts).

## Automation / efficiency angles
- Build count lists in shelf-walk order with sub areas (e.g., Keg Cooler → Line 1–12, Back Stock). Mobile counters then just tap down the list.
- Use **Out of stock** rather than skipping an item, so it shows as zero and not **Not counted**. Not-counted items distort actual consumption.
- After each count, a manager checks the **Below Par** bucket on the mobile summary to build that day's order.
- Weekly: assign the bar manager the bar and keg list and the KM the kitchen list, so both counts run in parallel on two phones.

## Related articles
- Inventory Counts: https://intercom.help/toast-central/en/articles/14727473-xtrachef-inventory-counts
- Get Started With Inventory Area Setup and Count Lists: https://intercom.help/toast-central/en/articles/14728252-xtrachef-get-started-with-inventory-area-setup-and-count-lists
- Get Started With Inventory Reports: https://intercom.help/toast-central/en/articles/9308181-xtrachef-get-started-with-inventory-reports
- Daily Sales on Mobile: https://intercom.help/toast-central/en/articles/14727713-xtrachef-daily-sales-on-mobile
- Help Center: xtraCHEF by Toast: https://intercom.help/toast-central/en/articles/14486883-help-center-xtrachef-by-toast
- Inventory Analytics: https://intercom.help/toast-central/en/articles/14727647-xtrachef-review-inventory-analytics
