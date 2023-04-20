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

    def play_game(self):
        while self.deck and not self.won():
            last_played_stone = self.discarded_stones.pop() if self.discarded_stones else None
            print(f"{self.current_player}\ndiscarded {last_played_stone}")
            # Ask all players if they want to take the "last_played_stone"
            all_decisions = self.players_decide(last_played_stone)
            selected_player_and_decision = self.pick_decision(all_decisions)  # <Player><Decision>

            if selected_player_and_decision is not None:
                self.current_player = selected_player_and_decision[0]

                print(f"{self.current_player.name} took  {last_played_stone} with {selected_player_and_decision[1]}")

                self.tick(last_played_stone, selected_player_and_decision[1][1])
                self.players.skip(self.current_player)
            else:
                if last_played_stone:
                    self.discarded_stones += [last_played_stone]
                print("discarded: ", self.discarded_stones)
                self.current_player = self.players.next()
                self.tick()
            print("")
        if self.won():
            print("\nPlayer won\n")
        else:
            print("\nNo more cards left\n")
        for players in self.players:
            print(players)

    def tick(self, stone=None, decision=None):
        if stone:
            discarded_stone = self.current_player.play(stone, decision)
        else:
            stone = self.deck.get_stone()
            discarded_stone = self.current_player.play(stone)
        self.discarded_stones.append(discarded_stone)
        return self

    def won(self):
        for player in self.players:
            if player.hu():
                return True
        return False

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
            # streak <- ('chi',(Stone(...),Stone(..))
            if streak is None:
                continue
            if streak[0] == "won":
                highest_player = player
                break
            elif streak[0] == "chi" and not highest_streak and next_player == player:
                highest_player = player
                highest_streak = streak
            elif streak[0] == "pong":
                highest_player = player
                highest_streak = streak
            elif streak[0] == "kong":
                highest_player = player
                highest_streak = streak
        if highest_player and highest_streak:
            return highest_player, highest_streak


if __name__ == '__main__':
    game = Game(["Albert Einstein", "Terminator", "ReadyPlayerOne", "Bob der Barrister"])
    game.play_game()
