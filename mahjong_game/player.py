from mahjong_game.stone import Stone


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def sort_hand(self):
        self.hand.sort()

    def play(self, stone):
        self.hand += [stone]
        self.sort_hand()
        if self.hu():
            return None
        index = self.decide()
        discard_stone = self.discard_stone(index)
        return discard_stone

    def decide(self):
        return 0  # TODO: index

    def discard_stone(self, index):
        return self.hand.pop(index)

    def decide_to_play(self, stone):
        if self.is_winning_tile(stone):  # winning stone has to be added to hand to check new hand will win
            return self, 'won'
        options = self.get_options(stone)
        if options:
            print(options[0])
            # TODO: add player logic do decide what to take
            return self, options[0][0]
        # return an option
        return self, None

    def is_winning_tile(self, stone):
        # add stone to copy of hand and check if it passes the winning format
        return True

    def get_options(self, stone):
        options = []
        if self.hand.count(stone) == 3:
            options += [('kong', (stone, stone, stone))]
        elif self.hand.count(stone) == 2:
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
        return self.hand.count(stone) != 0

    def __str__(self):
        return f"{self.name}: {self.hand}"

    def hu(self):
        # TODO: Hand checker class has to check if hand has won

        return len(self.hand) == 14

    def __eq__(self, other):
        same_name = self.name == other.name
        same_hand = self.hand == other.hand
        return same_name and same_hand

    def __repr__(self):
        return str(self)
