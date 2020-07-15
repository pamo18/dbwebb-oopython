#!/usr/bin/env python3
# pylint: disable=no-else-return

"""
Node Class file
"""

class Node:
    """
    Node class
    """
    def __init__(self, letter=None):
        """init"""
        self.letter = letter
        self.children = {}
        self.complete_word = False
        self.frequency = False

    def get_letter(self):
        """returns key"""
        return self.letter

    def get_children(self):
        """returns dictionairy"""
        return self.children

    def has_frequency(self):
        """returns word frequency"""
        return self.frequency

    def add_child(self, letter, letter_node):
        """adds child to dictionary"""
        self.children[letter] = letter_node

    def is_complete(self):
        """returns bool"""
        return self.complete_word

    def set_complete(self):
        """Mark as a complete word"""
        self.complete_word = True

    def set_frequency(self, frequency):
        """Mark as a complete word"""
        self.frequency = frequency
