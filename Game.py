from Card import Card
from Player import Player
from random import shuffle
from statistics import stdev


class Game:
    def __init__(self):
        """
        Sets up players, game stats and prompts game start
        """
        # initializing player 1 and player 2
        self.p1 = Player()
        self.p2 = Player()

        # Game Statistics
        self.total_lay = 0
        self.total_tie = 0
        self.total_games = 0
        self.p1_wins = 0
        self.p2_wins = 0
        self.lay = 0  # how many cards in each game are laid down including ties
        self.tie = 0  # how many ties in each game
        self.rounds = 0  # each initial round of each lay of cards
        self.stats = []

        # prompt for game to start
        self.game_control()

    def start(self):
        """
        Resets lay and tie, creates temp deck to stock both players hands with 26 cards
        """
        self.lay = 0
        self.tie = 0
        self.rounds = 0
        deck = [Card(i, j) for i in range(0, 13) for j in range(0, 4)]
        shuffle(deck)  # randomize deck
        self.p1.reset(deck[:26])
        self.p2.reset(deck[26:])

    def response(self):
        """
        Requests input until valid response is given to play game or not
        :return: "y" (yes) or "n" (no)
        """
        resp = input("Play War? y/n\n")
        while resp not in {"y", "n"}:
            print("Invalid\n")
            resp = input("Play War? y/n\n")
        return resp

    def play_hand(self):
        """
        Plays one hand of war in which the card at the top of each hand is compared
        Recurses when cards are equal
        :return: True if p1 wins/p2 loses, False if p1 loses/p2 wins
        """
        if len(self.p1) == 0:
            return False
        elif len(self.p2) == 0:
            return True
        self.lay += 1
        c1 = self.p1.get_card()
        c2 = self.p2.get_card()

        print("P1:", c1, "P2:", c2)

        if c1 > c2:  # player 2 wins
            self.p1.add_cards([c1, c2])
            return True
        elif c1 < c2:  # player 2 wins
            self.p2.add_cards([c1, c2])
            return False
        else:  # war
            self.lay += 1
            if len(self.p1) == 0:
                self.p2.add_cards([c1, c2])
                return False
            elif len(self.p2) == 0:
                self.p1.add_cards([c1, c2])
                return True

            w1 = self.p1.get_card()
            w2 = self.p2.get_card()

            print("\nTIE\n")

            self.tie += 1
            if self.play_hand():
                self.p1.add_cards([c1, c2, w1, w2])
                return True
            else:
                self.p2.add_cards([c1, c2, w1, w2])
                return False

    def game_control(self):
        """
        Prompts for game and plays hands until one player has no cards in deck
        """

        # while self.response() == "y":
        for _ in range(1000):  # uncomment and try running your own amount of games

            self.start()
            while len(self.p1) != 0 and len(self.p2) != 0:
                print("\n\nRound", self.rounds, "\n")
                self.play_hand()
                print("\nPlayer1\n\tHand:", str(self.p1) + ", Total:", self.p1.total_cards())
                print("Player2\n\tHand:", str(self.p2) + ", Total:", self.p2.total_cards())
                self.rounds += 1

            self.total_games += 1
            self.total_lay += self.lay
            self.total_tie += self.tie
            self.p1_wins += 0 if len(self.p1) == 0 else 1
            self.p2_wins += 0 if len(self.p2) == 0 else 1
            self.stats.append(self.lay)

            print("\nGame Stats\n")
            print("Winner:", "Player 1" if len(self.p1) != 0 else "Player 2")
            print("Lay:", self.lay, "Tie:", self.tie)
            print("Total Lay:", self.total_lay, "Total Tie:", self.total_tie)
            print("Player 1 Wins:", self.p1_wins, "Player 2 Wins:", self.p2_wins)
            print("Total Games:", self.total_games, "Average Hand:", round(self.total_lay/self.total_games, 2), "\n")
            if len(self.stats) > 1:
                print("Standard Deviation:", stdev(self.stats))

        print("\nGoodbye.\n")


# war game prompt when Game class is the driver
if __name__ == "__main__":
    Game()
