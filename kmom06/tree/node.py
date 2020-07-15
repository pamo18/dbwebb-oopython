#!/usr/bin/env python3
# pylint: disable=no-else-return

"""
Node Class file
"""

class Node:
    """
    Node class
    """
    def __init__(self, key, value, parent=None):
        """init"""
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def has_left_child(self):
        """returns bool"""
        return self.left is not None

    def has_right_child(self):
        """returns bool"""
        return self.right is not None

    def has_both_children(self):
        """returns bool"""
        return self.left is not None and self.right is not None

    def has_parent(self):
        """returns bool"""
        return self.parent is not None

    def is_left_child(self):
        """returns bool"""
        return self is self.parent.left

    def is_right_child(self):
        """returns bool"""
        return self is self.parent.right

    def is_leaf(self):
        """returns bool"""
        return self.left is None and self.right is None

    def __lt__(self, other):
        """returns bool"""
        if isinstance(other, Node):
            return self.key < other.key
        else:
            return self.key < other

    def __gt__(self, other):
        """returns bool"""
        if isinstance(other, Node):
            return self.key > other.key
        else:
            return self.key > other

    def __eq__(self, other):
        """returns bool"""
        if isinstance(other, Node):
            return self.key == other.key
        else:
            return self.key == other
