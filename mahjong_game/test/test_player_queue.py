import unittest

from mahjong_game.player_queue import PlayerQueue


class TestPlayerQueue(unittest.TestCase):
    def test_next(self):
        q = PlayerQueue([1, 2, 3, 4])
        self.assertEqual(q.next(), 1)
        self.assertEqual(q.next(), 2)
        self.assertEqual(q.next(), 3)
        self.assertEqual(q.next(), 4)
        self.assertEqual(q.next(), 1)

    def test_skip(self):
        q = PlayerQueue([1, 2, 3, 4])
        q.skip(2)
        self.assertEqual(q.next(), 3)
        self.assertEqual(q.next(), 4)
        self.assertEqual(q.next(), 1)
        self.assertEqual(q.next(), 2)

    def test_skip_last(self):
        q = PlayerQueue([1, 2, 3, 4])
        q.skip(4)
        self.assertEqual(q.next(), 1)
        self.assertEqual(q.next(), 2)
        self.assertEqual(q.next(), 3)
        self.assertEqual(q.next(), 4)

    def test_skip_invalid(self):
        q = PlayerQueue([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            q.skip(5)

    def test_empty_queue(self):
        q = PlayerQueue([])
        with self.assertRaises(IndexError):
            q.next()

    def test_iterator(self):
        q = PlayerQueue([1, 2, 3, 4])
        players = []
        for player in q:
            players.append(player)
        self.assertEqual(players, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
