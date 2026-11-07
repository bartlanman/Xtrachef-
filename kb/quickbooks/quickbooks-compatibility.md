---
title: "xtraCHEF: QuickBooks Compatibility"
source: https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility
last_updated: 2026-05-29
area: quickbooks
---
## What it is (2-4 sentences)
Lists which QuickBooks editions work with xtraCHEF and what the integration does. xtraCHEF + QuickBooks lets you push reconciled invoices as **bills**, daily sales as **journal entries**, and (QBO only) payroll as a journal entry. US only.

## When you'd use it
- Before onboarding or switching QB editions; when you hit "Feature Not Supported".

## How to do it (numbered steps with exact menu paths, button and field names)
1. Check your QBO edition at accounts.intuit.com (or QB product page).
2. Confirm it's in the compatible list below.
3. Proceed to the QBO or Desktop integration setup article.

**QuickBooks Online**
- Not compatible: **Self Employed**, **Simple Start** (no integrations allowed).
- Compatible: **Essentials**, **Plus**, **Advanced**.

**QuickBooks Desktop** (uses Intuit **Web Connector**, a local process)
- Compatible: **Desktop Enterprise**; **Desktop for PC** – Pro, Pro Plus, Premier, Premier Plus.
- Pre-2015 Desktop and **Desktop for Mac**: no Web Connector support, but **IIF file transfers** can be configured as a workaround.

## Settings, options & permissions (which roles can do it)
- N/A — edition requirement. Availability: US only (not Australia, Canada, Ireland, UK).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Payroll journal entry sync to QB is **QBO only**.
- Beta note: a Toast Payroll ↔ QBO direct integration (payroll data only, no xtraCHEF needed) exists — see Toast Payroll's QBO integration article.
- Mac/old Desktop = manual IIF imports, no automation.

## Automation / efficiency angles
- Basic City uses QBO — confirm the plan is Essentials or higher (Plus recommended if you want class/location tracking for brewery vs taproom vs restaurant; Essentials lacks class tracking in QBO).
- If the QBO plan is ever downgraded to Simple Start, every extract will fail with "Feature Not Supported".

## Related articles (links)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [xtraCHEF: Get Started With QuickBooks Desktop Integration](https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration)
- [xtraCHEF: Switch QuickBooks Integrations](https://intercom.help/toast-central/en/articles/14487875-xtrachef-switch-quickbooks-integrations)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
