---
title: "xtraCHEF: Get Started With QuickBooks Online Sales Syncing"
source: https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing
last_updated: 2026-08-24
area: quickbooks
---
## What it is (2-4 sentences)
The core setup guide for connecting xtraCHEF to QuickBooks Online for **invoices and sales**. After connecting, xtraCHEF imports the QBO chart of accounts and vendors, sends reconciled invoices as **Bills**, deposits/returns as **Vendor Credits**, and posts daily Toast sales as a **Journal Entry**. Payroll is a separate setup (Payroll Accounting Sync).

## When you'd use it
- First-time QBO connection (Basic City's cutover from the prior tool).
- Re-mapping GLs/vendors or adding a location-level QBO company.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereq**: Onboarding Consultant enables QBO extract (or email support@xtrachef.com).

**Connect**
1. **gear icon > Account setup** (opens **Tenant Configuration**) → **Integrations** tab → **Connect to QuickBooks**.
2. Click the log-in button → enter QBO username/password → **Sign In** → choose company.
3. **Authorize** → wait for blue **Continue** (connected).

**Sync GL codes & categories**
1. QBO GLs import and are matched to xtraCHEF categories (22 defaults per tenant). Exact name matches auto-assign; map the rest.
2. **+ Add category** to create; **+ Add GL Code** in the drop-down creates the GL in QBO.
3. Every **active** category must map to a GL before continuing; deactivate unused ones (this unmaps their items). Use the **Purchases** column to spot unused categories.
4. **Continue**.

**Sync vendors**
1. Exact-match vendors auto-assign; map the rest; **Add vendor** creates in QBO.
2. Blue **Continue**.

**Final questions**
- Q1: date to start sending expenses to QBO (past or future).
- Q2: extract receipts to QBO? (recommended **No**).
- **Continue**.

**Location-level QBO** (separate company files under one QBO account; skip if one location)
- Requires consultant config, identical chart of accounts and identical vendor codes across companies (else separate tenants).
1. **gear icon > Locations** → location → **Edit Location Details** → **Integrations** tab → **Connect to QuickBooks** → sign in → **Save**.

**Import more vendors later**: **gear icon > Account Setup > Integrations > Vendor(s)** button, or **Vendors > Action > Import vendors from QuickBooks Online**.

## Settings, options & permissions (which roles can do it)
- QBO Essentials/Plus/Advanced required. Admin in QBO; Tenant Admin in xtraCHEF.
- Receipt extract off by default; Customer Care can enable.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- **Warning**: any GLs you created manually in xtraCHEF before connecting are **deactivated** during GL sync — GLs should originate in QBO.
- Bills include the invoice image, GL and vendor details.
- Automatic syncing only starts once Sales Setup is done and xtraCHEF's machine learning is built for your account; only **reconciled** invoices extract.
- Start date choice is key to avoiding duplicates with bills entered by the previous tool.
- Payroll module enablement is separate.

## Automation / efficiency angles
- Cutover: set expense start date = first day the old tool stopped pushing bills; check QBO for any bills with the same numbers in the overlap window.
- Clean QBO vendor list (merge duplicates) before the vendor match step so auto-match works.
- Keep categories lean — every active category needs a GL forever.

## Related articles (links)
- [xtraCHEF: QuickBooks Compatibility](https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
- [xtraCHEF: Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [xtraCHEF: Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
