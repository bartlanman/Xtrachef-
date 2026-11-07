---
title: "xtraCHEF: Sales Setup"
source: https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup
last_updated: 2026-08-20
area: sales-sync
---

## What it is
Sales Setup is the configuration page that controls how Toast sales are broken out inside xtraCHEF for reporting. For QuickBooks and Intacct users, it also controls how the automated **daily sales journal entry** is built and posted. It has two parts: **General** (posting rules) and **Sales mapping** (Toast categories → COGS groups and GL accounts).

## When you'd use it
- Right after Toast is connected.
- Whenever a new Toast sales category, tender type, discount or service charge appears. Unmapped items cause extraction failures.
- When you change how tips, Amex or revenue centers should post.

## How to do it
**Open it**: **gear icon** (top right) **> Sales Setup**. The page opens on **General**.

### General (QBO / Intacct users only; others skip to Sales mapping)
1. **Breakout by revenue center**: turn this on to post sales by Toast revenue center (Taproom, Patio, Events and so on).
2. **Discount handling**: choose **Post by sales category** (default), **Post by type**, or **Post by revenue center**. The last option needs revenue centers and step 1 turned on.
3. **Auto payout tips**: creates a cash payout entry that subtracts total tips from the day's cash. Use it if card tips are paid out in cash nightly. There's a sub-option for **Cash Tips only**.
4. **Auto-adjust journal**: on by default with a **$10** threshold. Any over or short larger than the threshold posts as a "Cash Overage/Shortage" adjustment.
5. **Sales sync**: on by default. Once mapping is done, JEs post to accounting. If you turn it off, steps 6–8 disappear. Click **Save** to finish.
6. **Journal update frequency**: how many days back xtraCHEF re-updates prior sales JEs, **up to 30**. Set it to **0** if past entries shouldn't change.
7. **Payments/fees posting method**: **Post as total sum** or **Post by card type**.
8. **Amex posting method**: **Post as separate total sum**, or **Post with other credit cards** (default).
9. Click **Save** (top right). You can save at any point, and you must save before going to Sales mapping.

### Sales mapping
Open it with the **Sales mapping** button next to **Save** at the end of General. The tabs down the left start with Sales Categories, then (for accounting-connected tenants) **Tips, Discounts, Taxes, Service Charges, Payments, Payment Fees, Deferred, Adjustments, MCA Repayment**. Toast categories appear in the **Description** column.

10. **COGS mapping**: click each empty **COGS group** field and pick a group, or use **Create** / **+Create** to make a new one (it syncs to accounting where applicable). Click **Save**. Do the same on the **Discounts** tab. If you don't use QBO or QBD, Sales Setup is now finished.
11. **GL Description mapping**: for each row, pick a GL account. Suggestions tagged **Income** appear based on the description text. **View all GL types** shows every account, but use it carefully because it can skew the books.
   - Sales Categories → income accounts
   - Tips → tips-payable liability (whether tips are paid out as cash nightly or through payroll)
   - Discounts → contra-revenue or discount GL, or the same income GL if you don't track discounts separately
   - Tax → sales tax liability
   - Service Charges (auto gratuity, delivery fees) → liability
   - Payments (tenders) → clearing, bank or balance-sheet accounts depending on the tender
   - Payment Fees → merchant fee or withholding expense
   - Deferred (gift cards and similar) → the matching liability (Gift Card GL)
   - Adjustments (cash over/short, tip shortage) → an adjustment GL
   - MCA Repayment (Toast deductions from deposits, including DoorDash and Toast fees) → start with **Toast CC Withholding** (Other Current Asset)
12. Click **Save**. Mappings **don't** save automatically.
- **Bulk update**: tick the row checkboxes, then click **Bulk update** at the top to map many rows at once.

## Settings, options & permissions
- Opened from the gear menu. It's an account configuration task, which in practice means **Tenant Admin**.
- Prerequisites for the QBO sales sync: Toast is connected, QBO is connected, and Sales Setup is complete.

## Rules, limits & gotchas
- **Any unmapped field causes the sales extraction to fail.** Fix the mapping, then re-extract from **Sync Monitor**.
- If Sales sync is off, only the COGS mapping is needed, and the GL fields default to blank.
- With Journal update frequency above 0, past JEs can change after you've reconciled them. Consider setting it to a few days, or to 0 once a period is closed.
- The video in the article may show an older interface.

## Automation / efficiency angles
- For Basic City: map Visa/MC/Discover (and Amex, either combined or separate) to a **Toast CC Clearing** account rather than the bank account (see Resolving Unmatched Deposits). Map DoorDash and other third-party tenders to their own clearing accounts.
- Turn on **Breakout by revenue center** if the taproom, restaurant and events are separate Toast revenue centers. QBO then gets departmental sales without manual JEs.
- Make "new unmapped rows in Sales mapping" a weekly check. A new Toast discount or tender is the most common cause of a failed nightly sync.
- Use Bulk update when first mapping dozens of sales categories (one row per beer style, for example) to the same income GL.

## Related articles
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Review Analytics Reports](https://intercom.help/toast-central/en/articles/14727580-xtrachef-review-analytics-reports)
- [Resolving Unmatched Deposits](https://intercom.help/toast-central/en/articles/15705519-xtrachef-resolving-unmatched-deposits)
