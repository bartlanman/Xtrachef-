---
title: "xtraCHEF: Inbound Orders (Central Kitchen)"
source: https://intercom.help/toast-central/en/articles/14727539-xtrachef-inbound-orders-central-kitchen
last_updated: 2026-04-28
area: orders
---

## What it is
A **central kitchen** is a location that makes sauces, sides, or packaged goods for other locations. xtraCHEF lets the central kitchen publish **Internal Order Guides**, with optional markup. Other locations order from those guides, and the orders land in the central kitchen's **Inbound Orders** queue, where they're acknowledged and marked filled.

## When you'd use it
- When one location (for example, a main kitchen or the brewery) supplies another (for example, a taproom or event venue) with prepped food, sauces, or packaged product.

## How to do it
**Set up a central kitchen**
1. Email **support@xtrachef.com** or your account rep to designate the location. There's no limit on how many locations can be central kitchens. The location then shows **(Central Kitchen)** after its name.

**Create an internal order guide** (from the central kitchen location)
1. Go to **Order > Order Guide** (upper right). Central kitchens see an **Internal Order Guide** tab next to **Vendor Order Guide** and **Bid Sheet**.
2. Click **+ New Internal Order Guide**.
3. Configure it:
   - **Refresh item unit price**: daily, weekly, quarterly, or "Just in Time" (as the vendor updates).
   - **Overwrite item unit price**: toggle on (green) to let ordering locations change prices.
   - **Apply markup charges on all items**: a flat amount (for example, $5) or a percentage (for example, 5%) for delivery and labor. Ordering locations don't see it.
   - Choose which locations get access. **Available for all future locations** adds new locations automatically.
4. Click **Save**. Name the guide and add items: pick a vendor, then items. Items can also come from recipes, prep recipes, products, or individual invoice items.
5. Set the price and **minimum order** (at least 1). Check **Fixed Price** to stop the price from following supplier invoices. Click the blue **+**.
6. Click **Create Order Guide**. It's live immediately for the chosen locations.
7. To maintain guides, go to **Order > Order Guide > Internal Order Guide**, where each guide is a tile. Use **Edit** for items and minimums, **Configuration** for settings, access, and markup, and the trashcan to delete.

**Place an internal order** (from the receiving location)
1. Go to **Order**, click **Order**, and confirm the location.
2. In the left column choose **Order Guide**, then the guide under **Shared with You**. Items show **House Vendor - Location Name** as the vendor.
3. Add items with the blue **+**, click **Checkout**, enter the delivery date and shipping details, then click **Place Order**.

**Fulfill** (central kitchen)
1. Go to **Order**, select the central kitchen location, and open the **Inbound Orders** tab.
2. Click the **Order Number** for details.
3. Click **Acknowledge** to tell the requester you received it.
4. After delivering, click **Mark as filled**. This clears the order from pending and tells the location the goods are ready.

## Settings, options & permissions
- Support has to turn on central kitchen status.
- Recommended: all locations share the same accounting system, GL codes, and vendors.

## Rules, limits & gotchas
- **Inbound Orders shows one week at a time.** Page ahead to see upcoming deadlines.
- Once a location places an order from an internal guide, it **can't use that guide again until the order is filled**.
- **Fulfilling doesn't post to accounting or deplete inventory.** Record the intercompany transfer in QBO by hand and log depletion with **Manage Waste**.
- Markup is invisible to the ordering location.

## Automation / efficiency angles
- For Basic City this could model brewery-to-taproom or kitchen-to-Foundry-venue transfers. You'd still need a manual QBO transfer entry, so set a recurring month-end reminder to post them.
- Use **Fixed Price** for house-made items so their transfer price doesn't swing with supplier costs. Use **Just in Time** refresh for pass-through goods.
- Mark orders filled promptly. An unfilled order blocks that guide for the requesting location.

## Related articles
- [Order Guides](https://intercom.help/toast-central/en/articles/14727712-xtrachef-order-guides)
- [Create Orders](https://intercom.help/toast-central/en/articles/14727527-xtrachef-create-orders)
- [Order History](https://intercom.help/toast-central/en/articles/14726174-xtrachef-order-history)
- [Create Orders on Mobile](https://intercom.help/toast-central/en/articles/14727628-xtrachef-create-orders-on-mobile)
- GL Codes: https://central.toasttab.com/s/article/xtraCHEF-General-Ledger-Codes
- Inventory Waste: https://central.toasttab.com/s/article/xtraCHEF-Inventory-Waste
