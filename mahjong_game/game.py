from mahjong_game.deck import Deck
from mahjong_game.player import Player
from mahjong_game.player_queue import PlayerQueue


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

    def play_game(self, rounds_to_play=None):
        rounds = 0
        while self.deck and not self.won():
            if rounds == rounds_to_play:
                break
            last_played_stone = self.discarded_stones[-1] if self.discarded_stones else None
            self.current_player = self.pick_decision(self.players_decide(last_played_stone))  # None oder Chi etc
            if self.current_player:
                self.tick(last_played_stone)
                self.players.skip(self.current_player)
            else:
                self.current_player = self.players.next()
                self.tick()
            rounds += 1
            print(rounds, self.current_player)
        print('Game over')

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

        highest_player = None
        highest_streak = None
        next_player = self.players.next()
        self.players.skip(self.current_player)

        for player, streak in decisions:
            if streak == "won":
                highest_player = player
                break
            elif streak == "chi" and not highest_streak and next_player == player:
                highest_player = player
                highest_streak = streak
            elif streak == "pong":
                highest_player = player
                highest_streak = streak
            elif streak == "kong":
                highest_player = player
                highest_streak = streak
        return highest_player


if __name__ == '__main__':
    game = Game(["Albert Einstein", "Terminator", "ReadyPlayerOne", "Bob der Barrister"])
    game.play_game(30)
