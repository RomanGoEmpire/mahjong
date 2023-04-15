import unittest

from mahjong_game.player import Player
from mahjong_game.stone import Stone


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Initialize a player with a hand of 13 stones
        self.player = Player(name="Alice", hand=[Stone(1, "Dots"), Stone(2, "Dots"), Stone(3, "Dots"),
                                                 Stone(4, "Dots"), Stone(5, "Dots"), Stone(6, "Dots"),
                                                 Stone(0, "Red"), Stone(0, "Red"), Stone(0, "Red"),
                                                 Stone(1, "Bamboo"), Stone(2, "Bamboo"), Stone(2, "Bamboo"),
                                                 Stone(1, "Character")])

    def test_get_options(self):
        # Test case 1: Three of a kind
        options = self.player.get_options(Stone(1, "Dots"))
        self.assertEqual(options, [('chi', (Stone(2, "Dots"), Stone(3, "Dots")))], f"Test case 1 failed: {options}")

        # Test case 2: Pair
        options = self.player.get_options(Stone(2, "Bamboo"))
        self.assertEqual(options, [('pong', (Stone(2, "Bamboo"), Stone(2, "Bamboo")))],
                         f"Test case 2 failed: {options}")

        # Test case 3: Invalid stone
        options = self.player.get_options(Stone(9, "Character"))
        self.assertEqual(options, [], f"Test case 3 failed: {options}")

        # Test case 4: Chis
        options = self.player.get_options(Stone(2, "Dots"))
        self.assertEqual(options,
                         [('chi', (Stone(1, 'Dots'), Stone(3, 'Dots'))), ('chi', (Stone(3, 'Dots'), Stone(4, 'Dots')))],
                         f"Test case 4 failed: {options}")

        # Test case 5: Dragons
        options = self.player.get_options(Stone(0, "Red"))
        self.assertEqual(options,
                         [('kong', (Stone(0, 'Red'), Stone(0, 'Red'), Stone(0, 'Red')))],
                         f"Test case 5 failed: {options}")
