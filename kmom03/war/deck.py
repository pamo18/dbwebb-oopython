#!/usr/bin/env python3

"""
Deck klass
"""
import random
from card import Card

class Deck:
    """Deck of cards for War game"""
    def __init__(self):
        """init"""
        self.start = 0
        self.end = 13
        self.count = 4
        self.deck = []
        self.suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self.high_card = ["Jack", "Queen", "King", "Ace"]
        self.low_card = 2
        self.make_deck()
        self.shuffle_deck()


    def make_deck(self):
        """Create the deck of card objects"""
        for c in range(0, self.count):
            high = self.high_card
            low = self.low_card
            hc = 0
            for _card in range(self.start, self.end):
                if low <= 10:
                    make_card = Card(self.suit[c], low)
                    low += 1
                else:
                    make_card = Card(self.suit[c], high[hc])
                    hc += 1
                self.deck.append(make_card)

    def shuffle_deck(self):
        """Randomly shuffle the deck of card objects"""
        shuffled_deck = []
        deck_count = len(self.deck)
        for _card in range(0, deck_count):
            card_count = len(self.deck) - 1
            random_pos = random.randint(0, card_count)
            random_card = self.deck.pop(random_pos)
            shuffled_deck.append(random_card)
        self.deck = shuffled_deck

    def get_deck(self):
        """Returns the deck list of card objects"""
        return self.deck
