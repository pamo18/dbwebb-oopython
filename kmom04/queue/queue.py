#!/usr/bin/env python3

"""
Queue
"""

from exceptions import EmptyList
from node import Node

class Queue:
    """queue"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if list is empty
        """
        return self.head is None

    def enqueue(self, data):
        """
        Add item to queue
        """
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)

    def traverse(self):
        """
        Traverses through queue
        """
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def dequeue(self):
        """
        Removes item from queue
        """
        current = self.head
        try:
            if self.is_empty():
                raise EmptyList
            else:
                previous = current.data
                current = current.next
                self.head = current
                return previous
        except EmptyList:
            return "Not possible, empty list"

    def peek(self):
        """peek"""
        try:
            if self.is_empty():
                raise EmptyList
            else:
                show_first = self.head.data
                return show_first
        except EmptyList:
            return "Not possible, empty list"

    def size(self):
        """
        Return size of list
        """
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.get_next()

        return count
