import random

from mahjong_game.stone import Stone


class Deck:
    def __init__(self):
        self.stones = []
        self.create_deck()

    def create_deck(self):
        suits = ["Bamboo", "Dots", "Character"]
        honors = ["East", "South", "West", "North"]
        dragons = ["White", "Green", "Red"]
        for suite in suits:
            for i in range(1, 10):
                self.stones += [Stone(i, suite)]
        for honor in honors:
            self.stones += [Stone(0, honor)]
        for dragon in dragons:
            self.stones += [Stone(0, dragon)]
        self.stones *= 4
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.stones)

    def generate_hand(self):
        hand = self.stones[:13]
        self.stones = self.stones[13:]
        return hand

    def get_stone(self):
        stone = self.stones[0]
        self.stones = self.stones[1:]
        return stone

    def is_empty(self):
        return self.stones

    def __repr__(self):
        return str(self.stones)

    def __get__(self, index):
        return self.stones[index]

    def __set__(self, index, value):
        self.stones[index] = value

    def __iter__(self):
        return iter(self.stones)

    def __len__(self):
        return len(self.stones)
