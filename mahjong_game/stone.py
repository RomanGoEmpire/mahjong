class Stone:

    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
        rang = ["Dots", "Bamboo", "Character", "Green", "Red", "White", "East", "South", "West", "North"]
        self.rang = rang.index(suite) * 10 + value

    def __eq__(self, other):
        if not isinstance(other, Stone):
            return False
        same_value = other.value == self.value
        same_suite = other.suite == self.suite
        return same_value and same_suite

    def __repr__(self):
        return f"{self.value}_{self.suite}" if self.value != 0 else f"{self.suite}"

    def __gt__(self, other):
        return self.rang > other.rang

    def __ge__(self, other):
        return self.rang >= other.rang

    def __lt__(self, other):
        return self.rang < other.rang

    def __le__(self, other):
        return self.rang <= other.rang
