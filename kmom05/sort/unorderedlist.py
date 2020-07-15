#!/usr/bin/env python3

"""
Unordered list class
"""

from node import Node
from errors import EmptyList
from errors import CantFind
from errors import IndexTooHigh
from errors import IndexTooLow
from errors import NumbersOnly

class UnorderedList:
    """
    Unordered list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Checks if list is empty
        """
        return self.head is None

    def add(self, data):
        """
        Add item to list
        """
        current = self.head
        temp = Node(data)

        if current is None:
            self.head = temp
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(temp)

    def insert(self, index, data):
        """insert into"""
        current = self.head
        previous = None
        new_data = Node(data)
        counter = 0

        try:
            if self.is_empty():
                raise EmptyList
            elif not index.isdigit():
                raise NumbersOnly
            elif int(index) > (self.size()):
                raise IndexTooHigh
            elif int(index) < 0:
                raise IndexTooLow
            else:
                index = int(index)
                if index == 0:
                    new_data.set_next(self.head)
                    self.head = new_data
                else:
                    while counter < index:
                        previous = current
                        current = current.get_next()
                        counter += 1

                    new_data.set_next(previous.get_next())
                    previous.set_next(new_data)
                return data
        except EmptyList:
            print(("Empty list"))
        except IndexTooHigh:
            print(("Index position too high!"))
        except IndexTooLow:
            print(("Index position too low!"))
        except NumbersOnly:
            print(("Only numbers allowed!"))

    def set(self, index, data):
        """
        Set node-data in list at specific index
        """
        counter = 0
        current = self.head

        try:
            index = int(index)
            if self.is_empty():
                raise EmptyList
            elif int(index) > (self.size() - 1):
                raise IndexTooHigh
            elif int(index) < 0:
                raise IndexTooLow
            else:
                while index != counter:
                    temp = current.get_next()
                    current = temp
                    counter += 1
                current.data = data
                return current.data
        except ValueError:
            print(("Only numbers allowed!"))
        except EmptyList:
            print(("Empty list"))
        except IndexTooHigh:
            print(("Index position too high!"))
        except IndexTooLow:
            print(("Index position too low!"))


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

    def get(self, index):
        """
        Returns node data based on index
        """
        counter = 0
        current = self.head

        try:
            index = int(index)
            if self.is_empty():
                raise EmptyList
            elif index > (self.size() - 1):
                raise IndexTooHigh
            elif index < 0:
                raise IndexTooLow
            else:
                while index != counter:
                    temp = current.get_next()
                    current = temp
                    counter += 1
                return current.data
        except ValueError:
            print(("Only numbers allowed!"))
        except EmptyList:
            print(("Empty list"))
        except IndexTooHigh:
            print(("Index position too high!"))
        except IndexTooLow:
            print(("Index position too low!"))

    def index_of(self, value):
        """
        Returns index position if item found, else return False
        """
        counter = 0
        size = self.size()
        current = self.head
        found = "Not found!"
        while counter < size:
            if current.data == value:
                found = counter
            temp = current.get_next()
            current = temp
            counter += 1
        return found

    def print_list(self):
        """
        Prints each item in list
        """
        counter = 0
        size = self.size()
        current = self.head
        while counter < size:
            print(current.data)
            temp = current.get_next()
            current = temp
            counter += 1

    def remove(self, item):
        """
        Removes item from list
        """
        current = self.head
        previous = None

        try:
            if self.is_empty():
                raise EmptyList
            elif not self.is_found(item):
                raise CantFind
            else:
                while current.data != item:
                    previous = current
                    current = current.next

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return item
        except EmptyList:
            print(("Empty list"))
        except CantFind:
            print(("Not found"))

    def is_found(self, value):
        """
        Returns True if item found, else return index position
        """
        counter = 0
        size = self.size()
        current = self.head
        found = False
        while counter < size:
            if current.data == value:
                found = True
            temp = current.get_next()
            current = temp
            counter += 1
        return found
