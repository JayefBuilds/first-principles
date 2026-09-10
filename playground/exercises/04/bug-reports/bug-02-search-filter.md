# Cleared region filter still hides EU results

Reported by quality engineering on 2026-08-30.

## User report

A tester selected the `North America` region on the catalog page, then cleared the filter with the visible close button. The filter chip disappeared, but products available only in the EU remained absent from the results. Opening the catalog in a new private window showed the EU products again.

## Observed evidence

The captured request after clearing the filter still contains `region=na`. The page shows no active region chip at that moment. A fresh private window sends the same request without the region query and returns 84 products instead of 51.

## Available environment details

Staging web catalog. The report does not include the browser name, browser version, account identifier, console output, or the steps used before the region was first selected.
