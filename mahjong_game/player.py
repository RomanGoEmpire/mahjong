import random

from mahjong_game.hand_checker import HandChecker
from mahjong_game.stone import Stone


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.concealed_hand = hand
        self.melded_hand = []

    def sort_hand(self):
        self.concealed_hand.sort()

    def play(self, stone, other=None):
        print(self.name)
        print(f"took {stone}")

        if other:
            melded_stones = [stone] + list(other)
            melded_stones.sort()
            self.melded_hand += [melded_stones]
            for concealed_stone in other:
                self.concealed_hand.remove(concealed_stone)
        else:
            self.concealed_hand += [stone]
            self.sort_hand()

        if self.hu():
            return None

        index = self.decide()
        discard_stone = self.discard_stone(index)
        print(self.concealed_hand,len(self.concealed_hand))
        print(self.melded_hand,len(self.melded_hand))
        print(f"discarded {discard_stone}")
        return discard_stone

    def decide(self):
        return random.randint(0, len(self.concealed_hand) - 1)  # TODO: index

    def discard_stone(self, index):
        return self.concealed_hand.pop(index)

    def decide_to_play(self, stone):
        possible_hand = self.concealed_hand + self.melded_hand + [stone]
        if HandChecker().is_winning_hand(possible_hand):
            return self, 'won'
        options = self.get_options(stone)
        if options:
            # TODO: add player logic do decide what to take
            return self, options[0]  # currently selects the first decision
        # return an option
        return self, None

    def get_options(self, stone):
        options = []
        if self.concealed_hand.count(stone) == 3:
            options += [('kong', (stone, stone, stone))]
        elif self.concealed_hand.count(stone) == 2:
            options += [('pong', (stone, stone))]

        if stone.rang >= 30:
            return options

        stone_minus_2 = Stone(stone.value - 2, stone.suite)
        stone_minus_1 = Stone(stone.value - 1, stone.suite)
        stone_plus_1 = Stone(stone.value + 1, stone.suite)
        stone_plus_2 = Stone(stone.value + 2, stone.suite)

        if not self.contains(stone_minus_1) and not self.contains(stone_plus_1):
            return options

        if self.contains(stone_minus_1) and self.contains(stone_minus_2):
            options += [('chi', (stone_minus_2, stone_minus_1))]

        if self.contains(stone_minus_1) and self.contains(stone_plus_1):
            options += [('chi', (stone_minus_1, stone_plus_1))]

        if self.contains(stone_plus_1) and self.contains(stone_plus_2):
            options += [('chi', (stone_plus_1, stone_plus_2))]
        return options

    def contains(self, stone):
        return self.concealed_hand.count(stone) != 0

    def __str__(self):
        return f"{self.name}: {self.concealed_hand}"

    def hu(self):
        # TODO: Hand checker class has to check if hand has won

        return False

    def __eq__(self, other):
        same_name = self.name == other.name
        same_hand = self.concealed_hand == other.concealed_hand
        return same_name and same_hand

    def __repr__(self):
        return str(self)
