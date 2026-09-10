# TICKET-101 — Refresh lobby join codes

Players sometimes share a join code after it has expired. Add a way for the lobby owner
to refresh the code so friends can still join without recreating the lobby.

The refreshed code should be usable immediately and should not weaken the existing
expiration behavior.

## Why this ticket needs engineering judgment

The request does not specify whether the code value changes, what happens to the old code,
who besides the owner can refresh it, or how repeated refreshes behave. Treat those as
questions to surface, not permission to invent requirements.

