# Incident timeline

All times are UTC on 2026-08-14.

## Detection

* 14:03: Regional configuration rollout completed.
* 14:07: Checkout confirmation error alert fired for EU West.
* 14:11: On call acknowledged the alert and opened the incident channel.

## Investigation

* 14:15: Payment authorization was confirmed healthy.
* 14:19: The confirmation worker was restarted. The error rate did not change.
* 14:23: Regional route responses were compared with the active configuration.

## Recovery

* 14:27: The EU West route cache was cleared.
* 14:29: Confirmation success began to recover.
* 14:34: Confirmation success returned to baseline.
