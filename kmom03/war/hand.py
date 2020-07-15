#!/usr/bin/env python3

"""
Hand klass
"""

class Hand:
    """Players hand for War game"""
    def __init__(self, player):
        """init"""
        self.player = player
        self.player_hand = "Need to split the deck first"

    def get_hand(self):
        """Returns the players hand"""
        return self.player_hand

    def set_hand(self, hand):
        """Sets the players hand"""
        self.player_hand = hand

    def get_player(self):
        """Returns the players name"""
        return self.player
