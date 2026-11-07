---
title: "xtraCHEF: Approvals"
source: https://intercom.help/toast-central/en/articles/14726182-xtrachef-approvals
last_updated: 2026-08-20
area: invoicing
---

## What it is
Approval rules add a human checkpoint to otherwise automated invoice processing. When an invoice matches a rule (for example, over a dollar threshold, from a certain vendor, or above contract price), it pauses in **Ready to approve** until the assigned approvers act. Rules can have several approval levels and optional auto-approval.

## When you'd use it
- Controlling large or unusual spend, such as invoices over $2,000 or equipment repairs.
- Watching for contract price increases from broadline distributors.
- Reviewing manually entered invoices, which carry fraud or typo risk.
- Event and holiday orders flagged by invoice date.

## How to do it
**Create a rule** (requires **Tenant Admin**)
1. Click the **gear icon** (top right), then **Approval rules**.
2. Click **Create** under a rule type:
   - **Multi Condition**: any combination of vendor, location, invoice items, and invoice fields (amount, freight).
   - **Invoice Amount**
   - **Vendor Name**
   - **Invoice Date** (for example, holiday or large-event orders)
   - **Invoice Header Values** (for example, shipping fees or discount codes)
   - **Contract Price Variance**: flag goods priced above the agreed contract price, *or* alert on every price change (your choice).
   - **Manual Upload**: requires approval when someone keys in an invoice instead of scanning it.
   - **Cost Center**: flags expenses from Cost Centers. These rules are under a separate **Cost Center Rule** tab.
3. Set the criteria. Example: **Operator** = **Greater-Than (>)**, **Value** = **$2000.00**, then click **Next**.
4. Locations: click locations on the left to move them to the participating list on the right. At least one is required. Click **Next**.
5. Approvers: at least one level and one approver are required. Use **+ Add level** for a chain (Level 1 reviews before Level 2, and so on). The **clock icon** turns on auto-approval for a level. The **pencil** edits a level and the **trash** deletes it. Click **Submit**.
6. Name the rule. It appears in the rule list right away.

**Approve invoices**
1. Approvers see a red badge on **Approvals** in the left sidebar. Click it to open the queue.
2. For expected invoices, click the **thumbs-up** under **Quick Approve**. Otherwise click the **book icon** under **Open** to review the scan and the parsed data.
3. Click the green **Approve** button. Use the **yellow buttons** to fix problems (such as a receipt scanned as an invoice, or a wrong vendor). Use the red **Reject** button with a reason to reject. A rejected invoice moves to the Rejected column and its data isn't used.

## Settings, options & permissions
- **Tenant Admin** is required to create rules.
- Approvers must be assigned in the rule.
- Optional auto-approve per level (clock icon).
- Approvals also work in the mobile app (More > Approvals).

## Rules, limits & gotchas
- **No-cost goods aren't supported.** A $0 line is removed, and a $0 invoice is rejected. Free samples, promo cases, and comped replacements don't show up in food cost, approvals, or inventory.
- **Buy-X-get-one-free:** don't add a $0 line. Raise the **Quantity** on the existing line to the total units received (for example, 7 instead of 6) and leave the total alone. That gives the right blended unit cost and inventory count.
- Invoices that are waiting on approval don't extract to accounting. An approver who falls behind becomes an AP bottleneck.

## Automation / efficiency angles
- Turn on **Contract Price Variance** for broadline vendors such as Sysco and PFG to catch price creep automatically. This complements the weekly PFG vs Sysco price check.
- Add a **Manual Upload** rule as a fraud and typo control for hand-keyed invoices.
- Use an **Invoice Amount** threshold so only big tickets need eyes, and Quick Approve the expected ones.
- Use multi-level chains with auto-approval on the lower level, so routine items flow while the owner still sees large ones.
- Keep the number of rules small. Every rule adds delay.

## Related articles
- [Mobile Approval](https://intercom.help/toast-central/en/articles/14727663-xtrachef-mobile-approval)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- Cost Centers: https://central.toasttab.com/s/article/xtraCHEF-Cost-Center
