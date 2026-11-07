---
title: "xtraCHEF: Order Guides"
source: https://intercom.help/toast-central/en/articles/14727712-xtrachef-order-guides
last_updated: 2026-04-28
area: orders
---

## What it is
**Order Guides** are curated per-vendor lists of approved invoice items with typical quantities. They reduce brand and size drift when different people order. You can build guides by hand, import a vendor's **bid sheet** spreadsheet as a guide, and **schedule** a guide to submit itself to the vendor's rep automatically.

## When you'd use it
- To standardize recurring orders and reduce ordering mistakes.
- To load a vendor's price list or bid sheet.
- To automate standing weekly orders.

## How to do it
**Create a guide**: **Order > Order Guides**
1. Click **+ New Vendor Order Guide**. A draft named "New Order Guide" opens. Rename it under **Order Guide Name**.
2. Pick a **vendor** on the left, select the **Invoice Item(s)**, enter the usual **Quantity**, and click **+**.
3. Repeat for any vendor. Items you add appear on the far right.
4. Click **Create Order Guide**.

**Edit**: click **Edit**, add items or remove them with the trash can, then click **Update Order Guide**.

**Schedule (order automation)**: click **Schedule** on the guide and fill in:
- **Submission Days** (days of the week)
- **Start** / **End Date**
- **Schedule at** (time)
- **Note** (optional)
- **Auto Submission**: sends the guide to the vendor's sales reps automatically on that schedule.

**Upload a bid sheet**: **Order Guides > Bid Sheets**
1. Click **Upload Bid Sheet**, search for and select the vendor, then click **Next**.
2. Drop or pick a **.csv, .xls, or .xlsx** file and click **Next**.
3. Map the columns. The checkboxes are **Has Headers**, **Ignore Row without Unit Price**, **Ignore Row without Invoice Item Code**, and **Ignore Row without UOM**. The drop-downs map **Invoice Item Code**, **Invoice Item Description**, **UOM**, **Pack/Size**, and **Unit Price**.
4. Click **Next** to preview, then **Import Bid Sheet**. It now works as an order guide.
5. To edit a bid sheet: **Bid Sheets > Edit**, change quantities or remove items, then click **Update Order Guide**.

**Use a guide**: **Order**, then choose **Order Guide** instead of **Catalog**.

## Settings, options & permissions
- No roles are stated.
- Sales rep details must be on the vendor in the **Vendors** hub before you can schedule.

## Rules, limits & gotchas
- **Items that haven't been through Item Review don't appear** in guides.
- Scheduling fails with **Missing sales representative details** if the vendor has no rep information. Add it in the Vendor Hub (vendor information section).
- A vendor has to exist in the Vendors hub before you can upload its bid sheet.
- Schedule only orders that **don't change week to week**, because Auto Submission sends without review.

## Automation / efficiency angles
- **Scheduled order guides with Auto Submission are the main order automation in xtraCHEF.** Use them for fixed standing orders such as paper goods, cleaning chemicals, CO2, or a weekly bread order.
- Import broadline bid sheets (Sysco, PFG) as guides. Refresh them periodically to compare vendor pricing and feed the PFG vs Sysco price check.
- Turn on the import "ignore" filters so blank or partial rows from vendor exports don't create junk items.

## Related articles
- [Create Orders](https://intercom.help/toast-central/en/articles/14727527-xtrachef-create-orders)
- [Outbound Orders](https://intercom.help/toast-central/en/articles/14727717-xtrachef-outbound-orders)
- [Order History](https://intercom.help/toast-central/en/articles/14726174-xtrachef-order-history)
- [Inbound Orders (Central Kitchen)](https://intercom.help/toast-central/en/articles/14727539-xtrachef-inbound-orders-central-kitchen)
- [Get Started With Multi-Unit Onboarding](https://intercom.help/toast-central/en/articles/14487684-xtrachef-get-started-with-multi-unit-onboarding)
- Item Review: https://central.toasttab.com/s/article/xtraCHEF-Item-Review
- Vendor Hub: https://central.toasttab.com/s/article/xtraCHEF-Vendor-Hub
