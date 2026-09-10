# Lobby product behavior

The playground models a small multiplayer lobby. A player creates a lobby and becomes
its owner. Other players can join with the lobby's six-character join code.

## Join codes

- A newly created join code is valid for 15 minutes.
- The code becomes invalid at the expiration boundary, not one second later.
- A lobby holds at most four players, including its owner.
- A player already in the lobby cannot join it twice.
- A rejected join must not change membership.

## Invitations and blocking

- A player may invite another player unless the recipient has blocked the sender.
- Blocking is directional: Alice blocking Bob does not imply that Bob has blocked Alice.
- A blocked invitation must not be delivered to the recipient.

The product does not currently define user-facing copy, retry behavior, telemetry, or
whether blocked senders should receive a distinct error. Those are product decisions,
not details to infer from this document.

