---
title: "xtraCHEF: Set up QuickBooks Class or Location Tracking"
source: https://intercom.help/toast-central/en/articles/14727813-xtrachef-set-up-quickbooks-class-or-location-tracking
last_updated: 2026-04-22
area: quickbooks
---
## What it is (2-4 sentences)
How to make xtraCHEF bills and sales journal entries carry a QuickBooks **Class** or **Location** so you can run P&L by department/site in QBO. Class tracking tags each detail line; Location tracking tags the whole transaction. xtraCHEF supports only one of the two being on in QuickBooks.

## When you'd use it
- You want QBO P&L split by revenue area (e.g., brewery / taproom / kitchen) or by physical location.

## How to do it (numbered steps with exact menu paths, button and field names)
**Check which is on**: **Gear icon > Account Setup > Integrations** tab → checkboxes for **Class Tracking** / **Location Tracking**.

**Class Tracking**
1. **Gear icon > Classes** → sync classes from QuickBooks or **Add Class** manually.
2. **Gear icon > Locations** → select a location (turns blue) → **Edit Location Details** → enter the **class name** in **Account Number**.
3. **Gear icon > Sales Setup** → **Sales Mapping** → use the **Class** column to assign a class per sales category.

**Location Tracking** (QBO only)
1. Turn on location tracking in QBO.
2. **Gear icon > Locations** → select location → **Edit Location Details** → enter the QB **location name** in **Account Number**.

**Same QB login across locations with location-level QB enabled**: no tracking checkbox appears on Integrations. Instead import classes from QB, put the class in the location's account field (Edit Location Details), and map sales categories to classes.

## Settings, options & permissions (which roles can do it)
- Gear-menu settings (Classes, Locations, Sales Setup) — Tenant Admin.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Cannot have both Class and Location tracking on in QB for xtraCHEF.
- Location tracking best for multiple QB logins/company setups.
- Enter the class **name**, not its reference number, in Account Number; mismatch → "Location Account number is not assigned…" warning and bills post without class.
- Invoice class assignment is location-based only (one class per xtraCHEF location for bills); sales lines can get per-category classes.
- QBO Essentials does not offer class tracking (Plus/Advanced do).

## Automation / efficiency angles
- For a single-location brewery, consider classes per profit center (Beer production, Taproom, Kitchen, Events) on the sales side via Sales Mapping Class column.
- After setup, run a QBO "P&L by Class" and look for an "Not specified" column — that's untagged xtraCHEF activity to chase.

## Related articles (links)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [xtraCHEF: General Ledger (GL) Codes](https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
