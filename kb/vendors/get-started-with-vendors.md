---
title: "xtraCHEF: Get Started With Vendors"
source: https://intercom.help/toast-central/en/articles/14727525-xtrachef-get-started-with-vendors
last_updated: 2026-04-28
area: vendors
---

## What it is
The **Vendors** page (the **Vendor Hub**) is where you manage every vendor xtraCHEF knows about, whether synced from QBO or read from uploaded documents. It holds each vendor's **Vendor Code** (its accounting name), **Default Category**, **Extract Preference**, **Payment Terms**, **Approval Rule**, contacts, invoices, orders and statements.

## When you'd use it
- Fixing "Vendor does not exist in QuickBooks" extract errors.
- Setting a default GL for a vendor that always codes to one account (utilities, linen, propane, for example).
- Choosing summary-level or line-level extraction.
- Adding contacts for ordering.

## How to do it
**Browse**: left nav, **Vendors**. Active vendors show by default. The **Filter** drop-down adds inactive vendors or rebate vendors. Tick vendors, then use **Action** to make them active or inactive. **Download** exports the list.

**Vendor detail**: click the name in **Vendor Information**. The tabs are:
- **Overview**: addresses and contacts.
- **Configuration**: **Accounting** and **General** preferences for future documents. This is also where **Secondary Vendor ID** lives, which Fintech EDI uses.
- **Invoices**: recent invoices. Change **Invoice Date** or **Location** to see more.
- **Orders**: orders placed in xtraCHEF.
- **Statements**: Pro only.
- **Contacts**: needed for **Create Orders**, so order PDFs can be emailed to the rep.

**Inline columns on the list**
- **Vendor Code**: click the blank space in the column and type. It must **exactly match** the QBO vendor name (Display Name As), including capitalization, punctuation and spacing.
- **Default Category**: click the space and pick a GL or custom category. All future invoices from this vendor code to it.
- **Extract Preference**: **xtraCHEF Default** (decided per invoice, detail or summary), **Purchase Detail** (line items, always), or **Purchase Summary** (header totals only, always).
- **Payment Terms**: click the space to set. These can sync from accounting.
- **Approval Rule**: shows **Configured** if a rule applies (click it to view). There are none by default. See Approvals.

**Add a vendor**
1. Click **+ Add Vendor**.
2. **Overview**: name, address and so on. If there's no address, tick **Address information not available**, which fills the fields with "Not available".
3. **Configuration**: Vendor Code, category, payment terms and so on.
4. **Contacts** (optional): sales rep or account manager. **+ Add Contact** adds more.
5. Click **Save**.

## Settings, options & permissions
- View or edit vendor details: TA, EX, RM. Assign payment terms to a vendor: TA and RM. Create payment terms: TA.

## Rules, limits & gotchas
- A mismatched Vendor Code is the number one cause of failed invoice extracts.
- A Default Category overrides per-item coding for that vendor, which is fine for single-purpose vendors but wrong for broadline distributors that sell food, paper and chemicals.
- **Purchase Summary** means no line items, so no price tracking or item library entries for that vendor. Use it only for non-inventory vendors.

## Automation / efficiency angles
- For Basic City:
  - Set **Purchase Summary + Default Category** for utilities, rent, services, linen, pest control, propane and CO2/gas (unless you want CO2 cost per keg). These code themselves.
  - Keep **Purchase Detail** for PFG, Sysco, produce and beer, wine and spirits distributors, so the price tracker and recipe costs work.
  - Run a monthly Vendor Hub **Download** and compare Vendor Code with the QBO vendor list (the QBO connector can list vendors). Fix mismatches before they fail an extract.
  - Deactivate duplicate vendors created from OCR variants ("PFG", "Performance Foodservice", for example).

## Related articles
- [Set Up an EDI Integration With Vendors](https://intercom.help/toast-central/en/articles/9306947-xtrachef-set-up-an-edi-integration-with-vendors)
- [Order Guides](https://intercom.help/toast-central/en/articles/14727712-xtrachef-order-guides)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Tenant Configuration Settings](https://intercom.help/toast-central/en/articles/14728296-xtrachef-get-started-with-tenant-configuration-settings)
- [Extract Monitor](https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor)
