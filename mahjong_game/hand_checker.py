class HandChecker:

    def __init__(self, concealed_hand):
        self.concealed_hand = concealed_hand

    def is_winning_hand(self, hand=None):
        if not hand:
            hand = self.concealed_hand
        partitions = self.all_triple_partitions(hand)
        filtered = self.real_triples(partitions)
        for combo in filtered:
            result = self.check_combo(hand.copy(), combo)
            if result:
                return True
        return False

    def all_triple_partitions(self, hand):
        length = len(hand)
        combinations = []
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    combination = [hand[i], hand[j], hand[k]]
                    if combination not in combinations:
                        combinations.append(combination)
        return combinations

    def real_triples(self, partitions):
        filtered_partitions = []
        for partition in partitions:
            if self.is_chi(partition) or self.is_pong(partition):
                filtered_partitions += [partition]
        return filtered_partitions

    def check_combo(self, hand, combination):
        for stone in combination:
            hand.remove(stone)
        if len(hand) == 2 and hand[0] == hand[1]:
            return True

        partitions = self.all_triple_partitions(hand)
        filtered = self.real_triples(partitions)
        for option in filtered:
            conclusion = self.check_combo(hand.copy(), option)
            if conclusion:
                return True
        return False

    def is_pong(self, triple):
        return triple.count(triple[0]) == 3
