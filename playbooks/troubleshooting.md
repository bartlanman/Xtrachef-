# Troubleshooting — error → fix

Sources: `kb/quickbooks/quickbooks-extract-errors.md`, `kb/quickbooks/sales-sync-errors.md`, `kb/accounting/extract-monitor.md`.

## Bills (Extract Monitor → View Details → fix → Re-Extract)

| Error | Cause | Fix |
|---|---|---|
| Vendor '…' does not exist in QuickBooks / invalid reference to Vendor | Tenant Vendor Code ≠ QBO vendor **Display Name As** | Vendors → vendor → edit Tenant Vendor Code to match exactly → re-extract |
| Invalid reference to Account 'XCG-TAX' (or XCG-FC/OC/DC) | Header charges (tax, freight, discounts, other) have no distribution rule | Email support@xtrachef.com your choice: spread evenly, highest-cost GL, or a specific GL |
| Account '1234' does not exist in QuickBooks | GL name/number differs, or item in wrong category | gear > GL Codes → Edit GL Code to match QBO; or Item library → item → Category → Save Changes |
| AuthenticationFailed / 401 / Failed to Refresh Token | QBO token expired | gear > Account Setup > Integrations → Disconnect → Connect to QuickBooks (QBO Admin login). Redo whenever the QBO admin's password/email changes |
| String length … not supported | Invoice number > 21 characters | Search invoices → Edit Invoice → shorten → re-extract |
| Feature Not Supported | QBO edition lacks API | Needs Essentials, Plus or Advanced |
| Location Account number not assigned (warning) | Location not mapped to a QBO Class | gear > Locations → Edit Location Details → account number = Class name → re-extract |
| Payment '…' does not exist in QuickBooks | Receipt payment method name mismatch | Match QBO Settings > All Lists > Payment Methods exactly |
| There is no row at position 0 | Receipt has no payment method | Add payment method |
| Account period closed | Invoice dated in a closed period | Move invoice date into an open period |
| Invoice not in completed state | Invoice still Pending | Get it to Processed |
| Object reference not set to an instance of an object | Missing GL/category, vendor code or status | Check all three, re-extract |
| Matched Transaction Error | Bill matched to a bank feed transaction | Unmatch in QBO if appropriate, or adjust in QBO |

**Invoice never extracted?** Check: GL shows "Unassigned" (Map Invoice Items queue), stuck in Exception / Product Verification / Approvals, vendor code mismatch. Then **Extract Monitor > On-Demand Extract**.

**Clear RMS Reference** — only when the bill is NOT in QuickBooks. If it is, re-extracting creates a duplicate.

## Sales journal entries (Sync Monitor, red dot on a day)

| Alert | Fix |
|---|---|
| GL Mapping Needed | Map the new sales line in Sales Setup |
| Business Validation Error | Line mapped to an AP/AR GL — pick another GL |
| Data is modified after the previous sync | Toast changed after sync (voids, tip edits) — review, re-upload JE |
| Account does not exist in QuickBooks | Reassign lines to a current GL |
| Journal out of balance | Open check in Toast for that date — close it, resync |
| Object not found | Line mapped to inactive GL — use an active one |

Resync up to 7 days at once.

## Invoices
- Keeps reappearing → you clicked Reprocess; use **Submit Selected Items**.
- Duplicate rejection on vendors without invoice numbers → vendor Configuration > **Auto assign unique Invoice ID** (future uploads only).
- $0 lines/invoices unsupported → for "buy 6 get 1", set qty 7, same total.
- Doesn't balance → Invoiced Amount = Item Subtotal + Other Charges. Fix lines first, total last. Missing page → reject and re-upload, don't plug.
