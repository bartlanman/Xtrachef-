---
title: "xtraCHEF: Upload Invoices and Receipts on Mobile"
source: https://intercom.help/toast-central/en/articles/14727675-xtrachef-upload-invoices-and-receipts-on-mobile
last_updated: 2026-04-28
area: invoicing
---

## What it is
The xtraCHEF mobile app (iOS App Store / Google Play) can photograph invoices and receipts and send them straight into xtraCHEF processing, with no scanner needed. You can capture multiple pages, choose Invoice or Receipt, and record a credit during capture.

## When you'd use it
- Receiving deliveries at the back door: snap the invoice before the driver leaves.
- Staff buying supplies with a card (receipts).
- Any paper invoice that didn't arrive by email.

## How to do it
1. Install xtraCHEF from the App Store or Google Play and sign in.
2. On the **Mobile Dashboard**, tap the **Camera icon** at the bottom. This opens **Invoice Capture**.
3. Hold the phone parallel to the page. Use good light and a flat, contrasting background.
4. On the review/**Scan** screen:
   - **Add Page** (bottom-left): capture each additional page of the same invoice.
   - Document type: tap the drop-down by the default type at the top, choose **Invoice** or **Receipt**, then tap **Apply**.
   - **Credit**: record a credit memo or adjustment.
5. Tap **Submit** to upload.

After upload, the document goes into reconciliation, where it may be rejected (bad image, cropped, or missing pages), held in Action Needed (missing vendor code, invoice number, or date), or need line items mapped to GL codes and categories.

## Settings, options & permissions
- You need an xtraCHEF login with upload rights.
- Document type options: Invoice or Receipt.

## Rules, limits & gotchas
- **Every page of one invoice goes in one capture, using Add Page.** Separate photos are treated as separate invoices, which causes rejections, duplicates, or mismatched totals.
- **Credits: do one or the other.** If you hand-adjust the payable total on the paper *and* add a credit in the app, the credit is counted twice and you get "Invoice or line totals don't match."
- Images that are dark, blurry, or cropped get rejected.
- GL/category mapping is learned by machine learning. A new account has no learned mappings, so expect to code manually at first. xtraCHEF remembers each manual choice for future invoices.
- Analytics, budgets, and operating summaries only become meaningful once reconciliation is steady.

## Automation / efficiency angles
- Train receivers on one rule: one invoice equals one capture, with Add Page for each additional page.
- For vendors that email PDFs, prefer email-in or vendor integrations over photos. They're cleaner and cause fewer rejections.
- Set receipts to the Receipt type at capture, so you don't get missing-invoice-number exceptions.
- Coding manually early is an investment, because the ML reuses it. Code carefully in the first weeks.

## Related articles
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Track Invoice Status on the xtraCHEF App](https://intercom.help/toast-central/en/articles/14727570-xtrachef-track-invoice-status-on-the-xtrachef-app)
- [Approvals](https://intercom.help/toast-central/en/articles/14726182-xtrachef-approvals)
- Custom Categories: https://central.toasttab.com/s/article/xtraCHEF-Custom-Categories
- Mobile login: https://central.toasttab.com/s/article/xtraCHEF-Mobile-Logging-In
