---
title: "xtraCHEF: Inventory Counts"
source: https://intercom.help/toast-central/en/articles/14727473-xtrachef-inventory-counts
last_updated: "Updated over 2 weeks ago" (no calendar date shown)
area: count-lists
---
## What it is
This covers actually doing a scheduled count on desktop: opening the scheduled count, entering on-hand quantities, setting order amounts, submitting, and later editing or exporting it. xtraCHEF values the count automatically, and completed counts drive Beginning and Ending Inventory, COGS and analytics.

## When you'd use it
- On each scheduled count day (weekly or period-end).
- To go back and complete a missed or overdue count, or to correct a submitted one.
- To export a count with **Need to Order** values to place orders.

## How to do it
**Complete a scheduled count (desktop)**
1. Open the **Inventory** tab. It lands on **Inventory Counts**.
2. The calendar on the left shows the month's overdue and upcoming counts, plus today's. Click any date to finish a past count or preview a future one. If nothing is scheduled, you'll see "No inventory is scheduled."
3. Click the **down arrow** on the count, then **+ Add New Inventory**.
4. Click the **down arrow** again, then **Start**.
5. Enter quantities in the **UOM** column.
6. Adjust **Need to Order** as needed. It pre-fills when the count list has par levels.
7. For a product with several invoice items that differ in pack or size, open the product's **drop-down arrow** and count each item separately.
8. Click **Submit** (top right).

**Export order quantities:** on **Inventory Counts**, pick the day, click the count's **down arrow**, then **Download PDF** or **Download Excel**. The file includes **Need to Order**.

**Edit a submitted count:** go to the count's date, click the **arrow dropdown**, choose **Edit**, change the numbers and click **Submit**. Edits are valued at the prices that applied on the original count date.

## Settings, options & permissions
- No roles are stated in the article. See "Access to Inventory Features by Role" (kb/admin-and-users/inventory-access-by-role.md).
- Areas and count lists must already be set up.

## Rules, limits & gotchas
- **Counts are end-of-day.** A count and its value post to the **scheduled** date, no matter when the count is actually done.
- One item's quantity can't be more than **four digits**.
- If the same product appears in more than one section of a count list, each section is a **separate entry**. xtraCHEF doesn't merge them while you enter or edit.
- The **Reopen** button has been retired. Use **Edit**.
- **Changing the date** of a completed count needs support: email support@xtrachef.com.
- A completed count shows **Beginning Inventory**, **Ending Inventory** and **Fluctuation**.

## Automation / efficiency angles
- Count at close, or if you count in the morning, schedule it for the previous business day (see Area Setup). That keeps counts lined up with sales depletion.
- The Excel export with Need to Order works as a ready-made order sheet. An agent can turn it into vendor-by-vendor order drafts.
- Partial kegs: if a keg product has items in both kegs and gallons, count full kegs by keg and the open keg by estimated gallons (for example from a keg scale) using the per-item drop-down.
- Keep the four-digit limit in mind for small-unit items like portion cups or napkins. Count those by case or sleeve.

## Related articles
- Get Started With Inventory Area Setup and Count Lists: https://intercom.help/toast-central/en/articles/14728252-xtrachef-get-started-with-inventory-area-setup-and-count-lists
- Mobile Inventory: https://intercom.help/toast-central/en/articles/14727545-xtrachef-mobile-inventory
- Get Started With Inventory Reports: https://intercom.help/toast-central/en/articles/9308181-xtrachef-get-started-with-inventory-reports
- Review Inventory Analytics: https://intercom.help/toast-central/en/articles/14727647-xtrachef-review-inventory-analytics
- Glossary and Terminology: https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology
- Train on Advanced Inventory: https://intercom.help/toast-central/en/articles/14487654-xtrachef-train-on-advanced-inventory
- Video: https://play.vidyard.com/571gkNpPYQcW5V1tLwzoDN
