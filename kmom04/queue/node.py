#!/usr/bin/env python3

"""
Node
"""

class Node:
    """
    Node class
    """
    def __init__(self, data):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Returns data
        """
        return self.data

    def get_next(self):
        """
        Gets next node
        """
        return self.next

    def set_data(self, newdata):
        """
        Sets current nodes data
        """
        self.data = newdata

    def set_next(self, newnext):
        """
        Sets next node
        """
        self.next = newnext
