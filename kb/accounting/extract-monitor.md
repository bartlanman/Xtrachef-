---
title: "xtraCHEF: Extract Monitor"
source: https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor
last_updated: 2026-04-22
area: accounting
---

## What it is
The Extract Monitor is the log and control panel for **invoice extracts** (bills, receipts and credits) going from xtraCHEF to the accounting system. You can see which batches and invoices succeeded or failed, re-extract failures, run an on-demand extract, and download CSV extract files for accounting systems other than QuickBooks. Sales JEs are tracked separately, in the **Sync Monitor**.

## When you'd use it
- Daily or weekly, to confirm every completed invoice reached QBO.
- When a bill is missing in QBO.
- After fixing a vendor or GL mismatch.
- To pull CSV extracts for a non-QBO system.

## How to do it
**View extracts**
1. In the left nav, click **Extract monitor**.
2. Choose **location**, **date range** and **extract type** (the target software). **From Date** can't go earlier than your sync start.
3. Click **Submit**. Batches appear with their status. One batch can hold several invoices.
4. In **Invoice Extract Status**, **green** means success and **orange** means failed. Click **View Details** to see the error for each invoice.

**Re-extract**
1. Fix the cause of the failure.
2. Select the batch, click **Re-Extract**, then **Yes**.
- There's a limit on how many invoices can be re-extracted at once, depending on the date range and invoice count.

**Change the extract (sync) start date**
1. **gear icon > Account Setup > Integration** tab.
2. Under **Sync from QuickBooks**, change **Sync Start Date**. Invoices dated before this date won't extract.
3. Optional: turn on **On Demand Extract Only**. Invoices then extract only when you trigger it manually.
- If QBO is enabled **at the location level**, Customer Care has to change the start date.

**On-demand extract**
1. In the Extract Monitor, click **On-Demand Extract**.
2. Review the qualifying (processed) invoices. Exclude any by invoice date or extract date.
3. Submit. This doesn't disturb the regular schedule.

## Error reference (cause → fix)
1. **Invalid vendor reference / "Vendor does not exist in QuickBooks"**: the xtraCHEF Vendor Code ≠ the QBO vendor's **Display Name As** (QBD: Vendor Name). Go to **Vendors**, search, edit **Vendor Code** to match exactly, then re-extract.
2. **"Account '1234' does not exist in QuickBooks"**: the GL isn't in QBO. Correct the GL code in xtraCHEF, or, if the wrong category was assigned to the item, change the item's GL or category in the Item Library. This affects every invoice using that GL.
3. **AuthenticationFailed / errorCode 003200 / 401**: usually an expired QBO token (sometimes a timeout). Re-extract. If it repeats, refresh the QBO token (see QBO Integration article, "tokens" section).
4. **"String length is either shorter or longer than supported"**: the invoice number is longer than QBO's **21-character** limit. In **Search invoices > View detail**, shorten **Invoice Number**, submit, then re-extract.
5. **"Feature Not Supported"**: the QBO edition doesn't support the API. **Simple Start and Self-Employed aren't supported.** Use **Essentials, Plus or Advanced**.
6. **Invalid reference to "XCG-TAX"** (also **XCG-FC, XCG-OC, XCG-DC**): these are the default placeholder GLs for header-level charges (**Sales Tax, Freight/Distribution, Discounts, Other Charges**). Email support@xtrachef.com with your preference: spread evenly across the invoice's GLs, put it all on the highest-cost GL, or send it to a specific GL.
7. **"Location Account number is not assigned … pushed without class"**: xtraCHEF only supports **location-based classes**. Import classes from QBO, then **gear icon > Locations > Edit > Location Details** and put the **Class Name** (not its ID) in the **account number** field. If QBO has both location and class tracking on, the account number maps to Location.
8. **"Payment 'XXXXX' does not exist in QuickBooks"**: the payment method name doesn't match. In QBO, check **Settings > All Lists > Payment Methods** (Name column) and make it match xtraCHEF exactly.
9. **"Invalid account type"**: the QBO account type or code differs from xtraCHEF. Fix it, then re-extract from Search invoices.
10. **"QuickBooks connection not established"**: connect QBO or QBD first.
11. **"There is no row at position 0"**: a **receipt (RC)** has no payment method. Go to **Search invoices > Search > View detail > Edit invoice > Payment Details**, pick a method, click **Submit Invoice**, then re-extract.
12. **"Account period closed"**: the invoice date falls in a closed accounting period. Change the invoice date to the open period (or reopen the period).
13. **Invalid reference to QuickBooks AP Account**: the GL differs between the systems. Make them identical.
14. **"Invoice not in completed state"**: change status from **Pending** to **Processed**.
15. **"Object reference not set to an instance of an object"**: check that the GL/category, vendor code and status are all set, then re-extract. If it persists, contact Customer Care.
16. **"Duplicate invoice"**: that invoice number already exists in QBO. Check QBO before forcing anything.

## Settings, options & permissions
- Extract Monitor (view export files) is available to **Tenant Admin and Restaurant Manager**.
- Sync Start Date and On Demand Extract Only are under Account Setup > Integration (Tenant Admin).

## Rules, limits & gotchas
- Invoices dated **before** the sync start date never extract. This matters for backdated invoices around a cutover.
- Header charges without a GL preference post to XCG-* placeholders, which fail unless those accounts exist in QBO.
- QBO's 21-character invoice number limit is a common failure with long distributor invoice IDs.

## Automation / efficiency angles
- **Weekly agent check**: run Extract Monitor for the last 7 days and all locations, count the orange rows, group them by error text, and apply the fix from the table above. Most fall into categories 1, 2 and 3.
- Set the header-charge preference once, by email to support. For example, freight to "Freight In" and tax spread evenly. This removes a whole class of failures.
- Keep a vendor-code crosswalk (xtraCHEF Vendor Code = QBO Display Name As). Any new QBO vendor rename breaks extracts.
- For the Shogo → xtraCHEF cutover: set Sync Start Date to the cutover date so older invoices aren't pushed twice.
- If the QBO token keeps expiring (401 errors), add a monthly reconnect check.

## Related articles
- [Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
- [Clear RMS Reference Feature for QuickBooks](https://intercom.help/toast-central/en/articles/14726363-xtrachef-clear-rms-reference-feature-for-quickbooks)
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
