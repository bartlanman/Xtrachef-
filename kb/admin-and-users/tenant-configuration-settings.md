---
title: "xtraCHEF: Get Started With Tenant Configuration Settings"
source: https://intercom.help/toast-central/en/articles/14728296-xtrachef-get-started-with-tenant-configuration-settings
last_updated: 2026-04-22
area: admin-and-users
---

## What it is
**Tenant Configuration** is the account-wide settings page under **gear icon > Account Setup**. It has four tabs: **Basic Details**, **Integrations**, **Order** and **Sales**. These control invoice review thresholds, the start of the week, credits, extract permissions, subscription payment, accounting periods, integration credentials, RM ordering and sales display.

## When you'd use it
- Initial setup, or tightening controls (review large invoices, stop RMs from running ad-hoc extracts).
- Changing the subscription payment card.
- Changing the sync start date.

## How to do it
Open **gear icon** (top right) **> Account Setup**. It opens on **Basic Details**.

**Basic Details**
- **Invoice Threshold Value**: invoices above this amount need manual review before approval.
- **Start Day**: the first day of the week used throughout xtraCHEF (Sunday, Monday and so on).
- **Custom Category**: on by default. Email support to stop TAs from creating custom categories.
- **Tenant Credit Entry** (checkbox): lets users enter credits while uploading an invoice.
- **Enable Product Threshold Notification** (checkbox): sends a notification when an uploaded invoice exceeds the threshold.
- **Enable Account Closing Date**: invoices uploaded after the set date need manual review before approval.
- **Extract Enabled**: shows the connected integrations. Email support to add one.
- **Disable On Demand Extract for Restaurant Manager** (checkbox): RMs can only rely on scheduled extracts (daily, weekly, monthly). Only TAs can trigger an extract on demand.
- **Enable Category Update on Approval** (checkbox): TAs can edit line-item categories on the Approvals page.
- **Payment** button: update the card used for the xtraCHEF subscription, then **Submit**.
- **Accounting Period** button (under Budgets): opens Accounting Periods (**+ Add New Period**, then **+ Add**).

**Integrations** (only shown when at least one integration exists): set up QBO, QBD or Intacct. This is where **Sync from QuickBooks > Sync Start Date** and **On Demand Extract Only** live (see Extract Monitor). Email support@xtrachef.com to add an integration.

**Order**: tick **Disable vendor catalog ordering for restaurant manager role**, then **Save**, to stop RMs placing vendor orders.

**Sales** (only if Toast POS is synced): controls how sales are displayed and whether accounting JEs use the same names and dates as Toast.

## Settings, options & permissions
- Tenant Configuration (invoice threshold, start day, credit entry) is **Tenant Admin only**.

## Rules, limits & gotchas
- The Start Day affects weekly analytics (Food Cost Weekly, Category Weekly). Set it to match how you review the week.
- The Account Closing Date works with month-end close. Turn it on after closing so late or backdated uploads get reviewed.

## Automation / efficiency angles
- For Basic City, suggested controls:
  - Set **Invoice Threshold Value** around the size of a typical large distributor order, so unusually big invoices get a second look.
  - Turn on **Tenant Credit Entry** so receivers record shorts and credits at the dock.
  - Turn on **Disable On Demand Extract for Restaurant Manager** so only the bookkeeper or owner pushes ad-hoc batches to QBO.
  - Set **Start Day** to match the Toast business week used for labor and sales review.
- After each month-end close, move the Account Closing Date forward (along with the accounting period).

## Related articles
- [Accounting Periods](https://intercom.help/toast-central/en/articles/14726130-xtrachef-get-started-with-accounting-periods)
- [Set Up an EDI Integration With Vendors](https://intercom.help/toast-central/en/articles/9306947-xtrachef-set-up-an-edi-integration-with-vendors)
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Sync With Toast Web](https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web)
- [Configure Sage Intacct Integration](https://intercom.help/toast-central/en/articles/14727719-xtrachef-configure-sage-intacct-integration)
