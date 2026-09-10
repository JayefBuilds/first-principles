"""In-memory multiplayer lobby rules used by the training exercises."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum


class JoinResult(str, Enum):
    JOINED = "joined"
    INVALID_CODE = "invalid_code"
    EXPIRED_CODE = "expired_code"
    LOBBY_FULL = "lobby_full"
    ALREADY_JOINED = "already_joined"


@dataclass(frozen=True)
class Player:
    player_id: str
    blocked_player_ids: frozenset[str] = frozenset()


@dataclass
class Lobby:
    lobby_id: str
    owner: Player
    join_code: str
    code_created_at: datetime
    max_players: int = 4
    members: list[Player] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.members:
            self.members.append(self.owner)


class LobbyService:
    CODE_LIFETIME = timedelta(minutes=15)

    def join_with_code(
        self,
        lobby: Lobby,
        player: Player,
        code: str,
        now: datetime | None = None,
    ) -> JoinResult:
        current_time = now or datetime.now(timezone.utc)

        if code != lobby.join_code:
            return JoinResult.INVALID_CODE
        if current_time >= lobby.code_created_at + self.CODE_LIFETIME:
            return JoinResult.EXPIRED_CODE
        if any(member.player_id == player.player_id for member in lobby.members):
            return JoinResult.ALREADY_JOINED
        if len(lobby.members) >= lobby.max_players:
            return JoinResult.LOBBY_FULL

        lobby.members.append(player)
        return JoinResult.JOINED

    def can_invite(self, sender: Player, recipient: Player) -> bool:
        """Return whether sender may issue an invitation to recipient."""
        return sender.player_id not in recipient.blocked_player_ids

