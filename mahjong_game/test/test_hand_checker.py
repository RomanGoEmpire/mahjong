import unittest

from mahjong_game.hand_checker import HandChecker
from mahjong_game.player import Player
from mahjong_game.stone import Stone


class TestHandChecker(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Alice", hand=[Stone(1, "Dots"), Stone(1, "Dots"), Stone(2, "Dots"), Stone(2, "Dots"),
                                                 Stone(3, "Dots"), Stone(3, "Dots"), Stone(4, "Dots"),
                                                 Stone(4, "Dots")])
        self.hand_checker = HandChecker(self.player.concealed_hand)

    def test_triple_partitions(self):
        self.setUp()
        self.assertTrue(self.hand_checker.is_winning_hand())
        hand = [Stone(1, "Dots"), Stone(1, "Dots"), Stone(2, "Dots"), Stone(2, "Dots"),
                Stone(3, "Dots"), Stone(3, "Dots"), Stone(4, "Dots"),
                Stone(5, "Dots")]

        self.assertFalse(self.hand_checker.is_winning_hand(hand))

        hand = [Stone(1, "Dots"), Stone(2, "Dots"), Stone(2, "Dots"), Stone(2, "Dots"),
                Stone(3, "Dots"), Stone(3, "Dots"), Stone(4, "Dots"),
                Stone(4, "Dots")]
        self.assertFalse(self.hand_checker.is_winning_hand(hand))
