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

## Current state (verified live 2026-11-12, Claude in Chrome) — supersedes the 2026-11-07 read below
- **Sales sync is ON and working. Do not ask Bart about turning it on.** Cutover from Shogo is done: Shogo's last daily JE was business date 2026-11-08; xtraCHEF's first daily sales JE is 2026-11-10 (memo "Daily sales journal created by xtraCHEF"). Nov 9 had no sales posted by either. No day was posted by both.
- **Sync monitor: business dates Nov 1–9 show "Sync pending." Never sync them** (Actions → Sync to QuickBooks) — Shogo already posted Nov 1–8, so syncing would double-count revenue. If possible, confirm the sales sync start date is 2026-11-10.
- Sales mapping is complete (setup checklist: "Assign GL codes in sales setup" ticked). Discounts post to sub-accounts POS Discounts:Taproom and POS Discounts:Sip City (created 2026-11-02 — intentional, by location). Sales lines also carry QBO classes (TAPROOM, SIP CITY); harmless. Tips post to SALARIES & WAGES:FRONT OF THE HOUSE, same as Shogo did.
- **Invoice extract to QBO is ON** (re-enabled 2026-11-04). A batch ran 2026-11-10; QBO correctly refused invoices already sent on 10/27 as duplicates ("same invoice number and date exists").
- The warning "Location Account number is not assigned in XtraCHEF" on every bill is **harmless — ignore it**. Basic City reports by location through the chart of accounts (see Known decisions), not QBO Location/Class.
- Labor shows $0 in Operating summary because time and labor live in 7shifts, not Toast. Expected; prime cost is computed outside xtraCHEF (7shifts labor + QBO COGS). Don't flag it as a fault.
- Open (as of 2026-11-12): card-paid vendors (Webstaurant) are being extracted as unpaid bills, duplicating the Amex charges already booked via Ramp — need to stop those vendors syncing as bills (find the per-vendor setting) and remove the duplicates in QBO (Bart approves deletes). Invoice queue: ~39 Action Needed, ~43 Rejected.

## Live configuration (read 2026-11-07, Claude in Chrome) — OUT OF DATE, see above
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

## Known decisions (Bart — settled, don't re-ask)
- **2026-11-12 · P&L is managed by location through its account line items** (e.g. Food Sales – Taproom / Foundry / Showroom / Sip City, Foundry Supplies, Sip City Supplies, POS Discounts:Taproom). Not through QBO Location/Class tracking. Map new items to the location-named account.
- **2026-11-12 · The kitchen carries all food sales and food COGS** in the books. Where food sells and its item cost come from Toast / xtraCHEF item-level reporting. One food COGS account is correct.
- **2026-11-12 · Webstaurant is paid at purchase** (card, booked from Amex via Ramp). Its invoices must never post to QBO as unpaid bills — keep them in xtraCHEF for COGS/price tracking only.
- **2026-11-12 · Use Claude in Chrome** (Bart's real Chrome, signed into Toast) for the live account, not the built-in browser.

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
