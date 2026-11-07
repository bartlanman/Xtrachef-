---
title: "xtraCHEF: Get Help With QuickBooks Extract Errors"
source: https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors
last_updated: 2026-07-07
area: quickbooks
---
## What it is (2-4 sentences)
The troubleshooting guide for invoice (bill) extracts from xtraCHEF to QuickBooks that fail or warn. You confirm success in the **Extract Monitor**, open **View Details** on any non-green batch, then match the error text to a fix. It also covers what to check when an invoice never extracted at all.

## When you'd use it
- Any non-green Invoice Extract Status in Extract Monitor.
- A bill you expected in QBO isn't there.
- Tokens expired / authentication failures.

## How to do it (numbered steps with exact menu paths, button and field names)
**Check success**: **Extract Monitor** → any status not green → **View Details** → read the error → apply fix below → re-extract.

**Invalid reference to vendor** — "There is an invalid reference to QuickBooks Vendor '…' in the Bill" / "Vendor '…' does not exist in QuickBooks"
- Cause: xtraCHEF **Tenant Vendor Code** ≠ QB vendor name.
1. Left menu **Vendors** → search vendor → click the **Tenant Vendor Code** to edit.
2. Make it match exactly: QBO **Display Name As**; QB Desktop **Vendor Name**. Click the **check button**.
3. Re-extract from Extract Monitor.

**Invalid reference to XCG-TAX** — "invalid reference to QuickBooks Account 'XCG-TAX' in the Bill"
- Cause: header-level charges (Sales Tax, Freight/Distribution, Discounts, Other Charges) have no real GL. Choose a distribution: spread evenly across the invoice's GLs, apply to the highest-cost GL on the invoice, or post to a specific QB GL. If nothing is set, xtraCHEF uses placeholder GLs **XCG-FC, XCG-OC, XCG-DC, XCG-TAX** (which don't exist in QB → error). Send your preference to support@xtrachef.com.

**Account does not exist** — "Account '1234' does not exist in QuickBooks" / "invalid reference to QuickBooks Account '1234'"
- Affects every invoice with that GL.
- Option 1 (GL right, named differently): **gear icon > GL Codes** (Tenant Admin only) → select GL → **Edit GL Code** → match QB → **Save**.
- Option 2 (wrong category on an item): **Item library** → filter by vendor → select item → change **Category** at bottom (GL updates automatically) → **Save Changes** → re-extract.

**AuthenticationFailed** — "message=AuthenticationFailed; errorCode=003200; statusCode=401"
- Expired QBO token or timeout. Re-extract first; if it recurs: **gear icon > Account setup > Integrations** → **Connect to QuickBooks** → sign in (QB Admin).

**String length** — "String length is either shorter or longer than supported by specification"
- Invoice ID over QBO's **21-character** limit. **Search invoices** → **Edit Invoice** → shorten Invoice Number to under 21 → submit → re-extract.

**Feature Not Supported** — QB edition lacks API (Self-Employed, Simple Start). Need Essentials/Plus/Advanced.

**Location Account number not assigned** (warning, bill still posts without class) — "Location Account number is not assigned in XtraCHEF. Bill has been pushed to QBO without any class assignment."
1. Tenant Admin: **gear icon > Locations** → location → **Edit Location Details**.
2. Set account number to match the QB Class name.
3. **Extract Monitor** → select file → **Re-Extract** (top right).

**Invoice never extracted — check:**
- GL mapping: **Search invoices** → click **Invoice #** → any GL showing **Unassigned** means items are in the vendor's **Map Invoice Items** queue.
- Processing state: may be stuck in **Exception**, **Product Verification**, or **Approvals** queue.
- Vendor code: in **Vendor Hub**, code must match QBO "Display Name As" / Desktop Vendor Name.
- Then run an **On-Demand Extract**: QBO → **Extract Monitor > On-Demand Extract** (top left; pop-up shows count). Desktop → manual Web Connector sync.

**Failed to Refresh Token** (Tenant Admin)
1. **Gear Icon > Account Setup** → **Quickbooks Integration** tab.
2. **Disconnect from QuickBooks** → **Connect to QuickBooks** → log in.
3. Run a manual sync to confirm.

**Matched Transaction Error** (can't delete because matched to a downloaded bank transaction in a different account)
1. Find it in QB → review match history → unmatch from the bank feed transaction if appropriate.
2. Retry in xtraCHEF sync monitor. If it must stay matched, adjust directly in QB instead.

## Settings, options & permissions (which roles can do it)
- GL code edits, Locations edits, and QuickBooks reconnect: **Tenant Admin**.
- Reconnecting QBO: QB **Admin** login.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Vendor names must match character-for-character.
- QBO invoice/bill number max 21 chars.
- Unset header-charge distribution = guaranteed XCG-* errors — set this during onboarding.
- Location/class mismatch is only a warning; bills post unclassed (can silently skew class P&L).

## Automation / efficiency angles
- Daily: open Extract Monitor for the past 7 days; anything orange gets fixed same day.
- Set header-charge distribution once (e.g., freight to a Freight-In GL, tax spread evenly) to eliminate a whole error class.
- When adding a new vendor in QBO, copy the exact "Display Name As" into xtraCHEF's vendor code.
- For vendors with long invoice numbers, edit to ≤21 chars at reconciliation time.
- Weekly reconciliation: compare xtraCHEF reconciled invoice totals by vendor for the week vs QBO **Unpaid Bills/Bill list** for the same dates — gaps = unextracted or duplicated bills.

## Related articles (links)
- [xtraCHEF: Extract Monitor](https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
- [xtraCHEF: Get Started With QuickBooks Desktop Integration](https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration)
- [Help Center: xtraCHEF by Toast](https://intercom.help/toast-central/en/articles/14486883-help-center-xtrachef-by-toast)
