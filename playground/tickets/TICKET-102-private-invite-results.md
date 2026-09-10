# TICKET-102 — Make blocked invitations privacy-safe

Today the lobby service only says whether an invitation is allowed. Add a result that a
caller can use when an invitation is rejected, while preserving the recipient's privacy.

The behavior must continue to respect directional blocking and must not expose a player's
block list.

## Why this ticket needs engineering judgment

The request does not define the result shape, whether blocked and unavailable recipients
look identical, or which component owns user-facing copy. Treat those as questions to
surface, not permission to invent requirements.

