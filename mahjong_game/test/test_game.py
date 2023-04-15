import unittest

from mahjong_game.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_names = ["Alice", "Bob", "Charlie", "Dave"]
        self.game = Game(self.player_names)

    def test_create_players_from_names(self):
        self.assertEqual(len(self.game.players), len(self.player_names))

    def test_deck_has_correct_number_of_stones(self):
        self.assertEqual(len(self.game.deck), 84)

    def test_player_queue_starts_with_first_player(self):
        self.game.play_game(1)
        self.assertEqual(self.game.current_player.name, self.player_names[0])

    def test_tick_adds_discarded_stone_to_list(self):
        self.game.play_game(1)
        self.assertEqual(len(self.game.discarded_stones), 1)

    # def test_won_returns_true_if_player_hu(self):
    #    self.game.players.current_player.points = 1000  # Alice wins with 1000 points
    #    self.assertTrue(self.game.won())

    def test_won_returns_false_if_no_player_hu(self):
        self.assertFalse(self.game.won())

    def test_play_game_stops_after_10_rounds(self):
        self.game.play_game(10)
        self.assertLessEqual(len(self.game.discarded_stones), 40)

    def test_pick_decision_returns_highest_streak_decision(self):
        decisions = [(self.game.players[0], "chi"), (self.game.players[1], "pong"), (self.game.players[2], "kong")]
        player = self.game.pick_decision(decisions)
        self.assertEqual(player, self.game.players[2])


if __name__ == '__main__':
    unittest.main()
