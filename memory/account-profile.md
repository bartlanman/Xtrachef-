# Basic City Beer Co. — xtraCHEF Account Profile

Fill in as we learn. Configuration and decisions only — no sensitive numbers (repo is public).

## Business
- Basic City Beer Co., Waynesboro, VA — brewery, taproom, kitchen; The Foundry (music venue) on campus.
- POS: Toast. Accounting: QuickBooks Online. Back office: xtraCHEF (switched from Shogo).
- Toast Web entry point: https://app.sa.toasttab.com/Business/Management/NewDashboard

## xtraCHEF setup (to confirm in the live account)
- [ ] Subscription tier / features enabled
- [ ] Locations / tenants configured
- [ ] Users and roles
- [ ] Accounting integration: QuickBooks Online — what syncs (invoices as bills? sales JE?)
- [ ] Sales sync from Toast — on/off, mapping status
- [ ] Accounting periods
- [ ] GL code map and purchase categories
- [ ] Vendors active (known: PFG, Sysco — more to list)
- [ ] Invoice intake methods in use (email, mobile upload, vendor integration)
- [ ] Inventory: count lists, frequency, storage areas
- [ ] Recipes built / recipe costing in use

## Known decisions
_(none recorded yet)_

## To verify in the live account (from the help-center read, 2026-11-07)
- [ ] Sync Start Date (gear > Account Setup > Integration) = Shogo cutover date — prevents double-posted bills.
- [ ] Header-charge distribution (tax/freight/discounts) set with support — otherwise XCG-* placeholder GL errors.
- [ ] Every vendor's Tenant Vendor Code exactly matches QBO "Display Name As".
- [ ] Payroll posts by ONE route only (Toast Web Finance > Accounting); xtraCHEF payroll sync off.
- [ ] Card payments mapped to a "Toast CC Clearing" balance-sheet account (Sales Setup > Sales mapping > Payments), separate clearing accounts for DoorDash / Uber Eats / Grubhub.
- [ ] Sales Setup "Journal update frequency" set low once periods are reconciled (it can rewrite up to 30 days).
- [ ] Accounting periods: 12 calendar months, set per location (locked once created).
- [ ] EDI requested for PFG and Sysco (dashboard tile); beverage distributors via Fintech.
- [ ] xtraCHEF Bill Pay stopped taking payments Aug 28, 2026 — check QBO for refunded payments / reopened bills; vendors re-set in Toast Web > Bill Pay > Vendors.
- [ ] Keg items set up per kb/inventory/item-library.md (½ bbl 15.5 gal, ¼ bbl 7.75, ⅙ bbl 5.16).
- [ ] Executive role — help center calls it read-only but its permissions table allows invoice/vendor edits; test before assigning.

## Open issues
_(none recorded yet)_
