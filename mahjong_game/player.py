class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def sort_hand(self):
        self.hand.sort()

    def play(self, stone):
        self.hand += [stone]
        self.sort_hand()

        index = self.decide()
        discard_stone = self.discard_stone(index)

        return discard_stone

    def decide(self):
        return 0  # TODO: index

    def discard_stone(self, index):
        return self.hand.pop(index)


    def decide_to_play(self, stone):
        # TODO: check if stone can be claimed
        # return what option is available
        return self, None

    def hu(self):
        # TODO: Hand checker class has to check if hand has won
        return False

    def __str__(self):
        return f"{self.name}: {self.hand}"

    def __eq__(self, other):
        same_name = self.name == other.name
        same_hand = self.hand == other.hand
        return same_name and same_hand
