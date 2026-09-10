# Checkout remains pending after payment retry

Reported by support on 2026-08-28.

## User report

A customer entered an expired card during checkout. The first payment attempt failed as expected. They updated the card and selected Retry. The payment provider showed the second charge as approved, but the order page stayed on `Payment pending` for more than ten minutes. Refreshing the page did not change the status.

## Observed evidence

The support recording shows the Retry button becoming disabled at 09:42:16. The order page continues to display `Payment pending` at 09:52:31. Support confirmed that the customer received an approval notification from the payment provider.

## Available environment details

Production web checkout, desktop browser. The report does not include a browser version, order identifier, payment request identifier, application logs, or network trace.
