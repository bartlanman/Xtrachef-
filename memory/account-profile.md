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

## Live configuration (read 2026-11-07, Claude in Chrome)
- QBO connected 10/26/2026 by Bart; token valid to 2/4/2027. Location + Class tracking enabled.
- QBO Extract enabled 10/26/2026. **Sync Invoices = OFF** (gear > Account setup > Integrations). Sync Start Date 10/26/2026. On Demand Extract Only = False.
- One extract ran 10/27/2026: 44 PFG bills (invoice dates Jul–Oct 2026) extracted to QBO vendor "PFG"; 2 Sysco Dec-2025 invoices failed "Account Period Closed". Every extracted bill warned "Location Account number is not assigned" (bills posted with no class).
- No extracts since 10/27 → invoices processed after that are not in QBO.
- **Sales sync = OFF** (Sync monitor banner). Toast sales are pulled into xtraCHEF daily but not pushed; QBO Nov sales are still arriving from Shogo.
- Vendor list imported from QBO (~1,350 active). PFG: vendor name "Performance Foodservice Virginia B2", Vendor Code "PFG", Extract Preference Purchase Detail.
- Vendors seen on invoices: PFG, Sysco, webstaurant, International Gourmet Foods.
- Duplicate detection working: re-uploaded PFG/webstaurant invoices were auto-rejected.
- Setup checklist 87%: remaining = sync sales to QBO, review Sync monitor, sync expenses to QBO, review Extract monitor.
- Operating Summary labor = $0 (payroll not flowing to xtraCHEF).

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
