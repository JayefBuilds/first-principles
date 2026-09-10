# Lobby API contract

The sample service is called directly in Python; there is no network server.

## `join_with_code(lobby, player, code, now=None)`

Returns exactly one `JoinResult`:

| Result | Meaning |
|---|---|
| `joined` | The player was added to the lobby. |
| `invalid_code` | The supplied code does not match. |
| `expired_code` | The matching code is no longer valid. |
| `lobby_full` | The lobby already contains its maximum number of players. |
| `already_joined` | The player is already a member. |

When more than one rejection condition is true, the first rule evaluated by the service
determines the result. Existing callers may rely on that result, so a change to precedence
requires an explicit product decision.

## `can_invite(sender, recipient)`

Returns a Boolean indicating whether an invitation is allowed. It does not send or store
an invitation.

