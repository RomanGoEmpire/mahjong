from collections import deque


class PlayerQueue:
    def __init__(self, elements):
        self.queue = deque(elements)
        self.size = len(elements)

    def next(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        element = self.queue[0]
        self.queue.rotate(-1)  # rotate the deque to the left
        return element

    def __len__(self):
        return self.size

    def skip(self, player):
        if self.size == 0:
            raise IndexError("Queue is empty")
        if player not in self.queue:
            raise ValueError("Player not in queue")
        while self.next() != player:
            pass  # keep calling next until we get to the specified player

    def __iter__(self):
        for player in self.queue:
            yield player

    def __getitem__(self, index):
        return self.queue[index]
