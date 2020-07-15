#!/usr/bin/env python3

"""
Unittest file for Phone
"""

import unittest
from hand import Hand
from deck import Deck
from card import Card

class Testwar(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.hand = Hand("Player 1")
        self.deck = Deck()
        self.card = Card("Hearts", 9)

    def tearDown(self):
        """ Remove dependencies after test """
        self.hand = None
        self.deck = None
        self.card = None


    def test_player_name(self):
        """Test for player name"""
        self.assertEqual(self.hand.get_player(), "Player 1")

    def test_empty_hand(self):
        """Test for empty hand"""
        self.assertEqual(self.hand.get_hand(), "Need to split the deck first")

    def test_set_hand(self):
        """Test for setting hand"""
        self.hand.set_hand(["Queen of hearts", "7 of Diamonds"])
        self.assertEqual(self.hand.get_hand(), \
        ["Queen of hearts", "7 of Diamonds"])

    def test_deck_size(self):
        """Test for 52 unshuffled card objects"""
        self.assertEqual(len(self.deck.get_deck()), 52)

    def test_reshuffle_deck(self):
        """Test to re-shuffle 52 card objects"""
        self.deck.shuffle_deck()
        self.assertEqual(len(self.deck.get_deck()), 52)

    def test_random_deck(self):
        """Test to see if shuffled deck is random"""
        deck_before = self.deck.get_deck()
        self.deck.shuffle_deck()
        self.assertFalse(self.deck.get_deck() == deck_before)

    def test_card_suit(self):
        """Test for card suit"""
        self.assertEqual(self.card.get_suit(), "Hearts")

    def test_card_value(self):
        """Test for card value"""
        self.assertEqual(self.card.get_value(), 9)


if __name__ == '__main__':
    unittest.main(verbosity=3)
