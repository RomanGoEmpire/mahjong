from deck import Deck
from player import Player
from player_queue import PlayerQueue


class Game:

    def __init__(self, player_names):
        self.deck = Deck()
        players = self.create_players_from_names(player_names)
        self.players = PlayerQueue(players)
        self.discarded_stones = []
        self.current_player = None

    def create_players_from_names(self, player_names):
        players = []
        for name in player_names:
            players.append(Player(name, self.deck.generate_hand()))
        return players

    def won(self):
        for player in self.players:
            if player.hu():
                return True
        return False

    def tick(self, stone=None):
        if not stone:
            stone = self.deck.get_stone()
        discarded_stone = self.current_player.play(stone)
        self.discarded_stones.append(discarded_stone)
        return self

    def play_game(self):
        rounds = 0
        while self.deck and not self.won():
            rounds += 1
            if rounds == 10:
                break
            last_played_stone = self.discarded_stones[-1] if self.discarded_stones else None
            self.current_player = self.pick_decision(self.players_decide(last_played_stone))

            if self.current_player:
                self.tick(last_played_stone)
                self.players.skip(self.current_player)
                continue

            self.current_player = self.players.next()
            self.tick()

            print(rounds, self.current_player)

    def players_decide(self, last_played_stone):
        if not last_played_stone:
            return []
        decisions = []
        for player in self.players:
            decisions.append(player.decide_to_play(last_played_stone))
        return decisions

    def pick_decision(self, decisions):
        if not decisions:
            return None
        return None  # TODO: check for pongs etc


if __name__ == '__main__':
    game = Game(["Albert Einstein", "Terminator", "ReadyPlayerOne", "Bob der Barrister"])
    game.play_game()
