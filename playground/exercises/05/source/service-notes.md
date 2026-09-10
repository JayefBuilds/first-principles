# Confirmation service notes

## Trigger

The 14:03 configuration rollout removed an obsolete route but did not invalidate the EU West route cache. Requests in that region continued using a stale destination. The same rollout completed in other regions without an error because their route caches had already expired.

## What did not work

The confirmation worker was restarted at 14:19. This did not change the error rate because the worker received the same stale route from the regional cache after restart.

## Recovery

The on call engineer cleared the EU West route cache at 14:27. New requests then resolved the active destination. Confirmation success began to recover at 14:29 and returned to baseline at 14:34.
