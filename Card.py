
class Card:

    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit_list = ['\u2663', '\u2666', '\u2665', '\u2660']

    def __init__(self, rank, suit):
        """ Initialize cards rank (1-14) and suit (spade, diamond, club or heart)"""
        self.__rank = rank
        self.__suit = suit

    def __str__(self):
        """ Convert card into a string (usually for printing)"""
        return "{}{}".format(self.rank_list[self.__rank], self.suit_list[self.__suit])

    def __repr__(self):
        """
        Used for terminal use and used to print lists of cards
        :return: string of card
        """
        return self.__str__()

    def __lt__(self, other):
        """
        :param other: card to compare
        :return: true if rank is less than, else false
        """
        return self.rank() < other.rank()

    def __gt__(self, other):
        """
        :param other: card to compare
        :return: true if rank is greater than, else false
        """
        return self.rank() > other.rank()

    def rank(self):
        """
        :return: rank of card (1-14)
        """
        return self.__rank
