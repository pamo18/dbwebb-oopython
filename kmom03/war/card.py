#!/usr/bin/env python3

"""
Card klass
"""

class Card:
    """Playing card class for war game"""
    def __init__(self, suit, value):
        """init"""
        self.suit = suit
        self.value = value

    def get_suit(self):
        """Return suit"""
        return self.suit

    def get_value(self):
        """Return value"""
        return self.value

    def __repr__(self):
        """Returns a string with cards suit and value"""
        return "{card_val} of {card_suit}".format(
            card_val=self.value,
            card_suit=self.suit)
