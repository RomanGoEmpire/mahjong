class Stone:

    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
        rang = ["Dots", "Bamboo", "Character", "Green", "Red", "White", "East", "South", "West", "North"]
        self.rang = rang.index(suite) * 10 + value
        self.is_dragon = self.suite in ["Green", "Red", "White"]
        self.is_wind = self.suite in ["East", "South", "West", "North"]
        self.is_terminal = value == 1 or value == 9

    def __eq__(self, other):
        if not isinstance(other, Stone):
            return False
        return self.rang == other.rang

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

    def __sub__(self, other):
        if isinstance(other, int):
            return Stone(self.value - other, self.suite)
        raise TypeError(f"cannot subtract type {type(other)} from stone ({self})")