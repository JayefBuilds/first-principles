from datetime import datetime, timedelta, timezone
import unittest

from src.lobby import JoinResult, Lobby, LobbyService, Player


class LobbyServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.created_at = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
        self.owner = Player("owner")
        self.lobby = Lobby("lobby-1", self.owner, "NOVA42", self.created_at)
        self.service = LobbyService()

    def test_player_joins_with_valid_code(self) -> None:
        result = self.service.join_with_code(
            self.lobby,
            Player("new-player"),
            "NOVA42",
            self.created_at + timedelta(minutes=1),
        )

        self.assertEqual(JoinResult.JOINED, result)
        self.assertEqual(["owner", "new-player"], [p.player_id for p in self.lobby.members])

    def test_wrong_code_is_rejected(self) -> None:
        result = self.service.join_with_code(
            self.lobby,
            Player("new-player"),
            "WRONG",
            self.created_at + timedelta(minutes=1),
        )

        self.assertEqual(JoinResult.INVALID_CODE, result)

    def test_code_at_expiration_boundary_is_rejected(self) -> None:
        result = self.service.join_with_code(
            self.lobby,
            Player("new-player"),
            "NOVA42",
            self.created_at + timedelta(minutes=15),
        )

        self.assertEqual(JoinResult.EXPIRED_CODE, result)

    def test_full_lobby_is_rejected(self) -> None:
        self.lobby.members.extend([Player("p2"), Player("p3"), Player("p4")])

        result = self.service.join_with_code(
            self.lobby,
            Player("p5"),
            "NOVA42",
            self.created_at + timedelta(minutes=1),
        )

        self.assertEqual(JoinResult.LOBBY_FULL, result)

    def test_recipient_can_block_invites_from_sender(self) -> None:
        sender = Player("sender")
        recipient = Player("recipient", frozenset({"sender"}))

        self.assertFalse(self.service.can_invite(sender, recipient))

    def test_unblocked_sender_can_invite_recipient(self) -> None:
        self.assertTrue(self.service.can_invite(Player("sender"), Player("recipient")))


if __name__ == "__main__":
    unittest.main()

