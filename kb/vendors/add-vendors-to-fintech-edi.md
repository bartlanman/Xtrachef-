---
title: "Add Additional Vendors to Your Fintech EDI"
source: https://intercom.help/toast-central/en/articles/10533397-add-additional-vendors-to-your-fintech-edi
last_updated: 2026-07-02
area: vendors
---

## What it is
Once your Fintech EDI link with xtraCHEF is live, **you** add each new distributor yourself. The distributor's vendor ID in the Fintech portal must match the **Secondary Vendor ID** on the vendor in xtraCHEF. When they match, Fintech invoices route to the right xtraCHEF vendor.

## When you'd use it
- Adding a new beer, wine or spirits distributor (or any Fintech-billed vendor).
- When invoices from one Fintech distributor stop arriving.

## How to do it
**Part 1: Fintech portal**
1. Log in at fintech.com.
2. Go to **Tools > My Distributors**.
3. Find the distributor (add it first if it isn't listed), then click **edit** on the right.
4. Set the vendor ID. It must be **unique, 10 characters or fewer, with no special characters**.
5. Click **Save**.
- Fintech isn't responsible for wrong ID changes. Fintech support: support@fintech.com, (800) 572-0854, option 1 (Client Services), then 1 (Client Support).

**Part 2: xtraCHEF**
1. Left nav, **Vendors**. Find the vendor or create it.
2. Click the vendor name, then the **Configuration** tab.
3. In **Secondary Vendor ID**, enter exactly the Fintech vendor ID.
4. Click **Save**.

## Settings, options & permissions
- Vendor editing is available to TA, EX, RM. You also need a Fintech portal login.

## Rules, limits & gotchas
- The IDs must match **exactly** in both systems.
- Still not receiving invoices with matching IDs? Email support@xtrachef.com with the **tenant name, affected locations and vendor**. Support works it out with Fintech.

## Automation / efficiency angles
- For Basic City: use a simple ID scheme such as a short distributor abbreviation plus a number (for example "VADIST01"), 10 characters or fewer with no symbols. Keep a crosswalk of distributor → Fintech ID → xtraCHEF vendor in `memory/` (IDs only, no amounts).
- Each time a new distributor is added in Fintech, do Part 2 the same day so no invoices get lost.

## Related articles
- [Set Up an EDI Integration With Vendors](https://intercom.help/toast-central/en/articles/9306947-xtrachef-set-up-an-edi-integration-with-vendors)
- [Get Started With Vendors](https://intercom.help/toast-central/en/articles/14727525-xtrachef-get-started-with-vendors)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Multi-Unit Onboarding](https://intercom.help/toast-central/en/articles/14487684-xtrachef-get-started-with-multi-unit-onboarding)
