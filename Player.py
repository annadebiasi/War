from random import shuffle


class Player:
    """Initializing player with hand and reserve"""

    def __init__(self):
        """Initialize hand and reserve piles of cards"""
        self.__hand = []  # cards in play
        self.__reserve = []  # winnings

    def __str__(self):
        """
        :return: string of hand
        """
        return str(self.__hand)

    def __len__(self):
        """
        :return: length of hand
        """
        return len(self.__hand)

    def total_cards(self):
        """
        Used for printing purposes only
        :return: length of hand & reserve
        """
        return len(self) + len(self.__reserve)

    def get_card(self):
        """
        Get card on top of hand and tries to restock
        :return: next card for play
        """
        card = self.__hand.pop()
        # if hand is ever empty, restock
        self.restock()
        return card

    def reset(self, hand):
        """
        Used in initial game play to set half of deck to hand and clear reserve hand
        :param hand: list of cards
        """
        self.__hand = hand
        self.__reserve = []

    def add_cards(self, card):
        """
        Adds cards to reserve as winnings
        :param card: list of cards
        """
        self.__reserve.extend(card)
        self.restock()

    def restock(self):
        """
        Restocks hand if empty and resets reserve
        """
        # on restock when hand is empty
        if len(self) == 0:
            shuffle(self.__reserve)  # randomize
            self.__reserve, self.__hand = [], self.__reserve
