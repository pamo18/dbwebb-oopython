#!/usr/bin/env python3

"""
Main
"""

from queue import Queue

class Handler:
    """
    Handler
    """
    def __init__(self):
        """init"""
        self.my_list = Queue()
        self.menu()

    def enqueue(self, choice):
        """add to"""
        self.my_list.enqueue(choice)

    def dequeue(self):
        """remove"""
        value = self.my_list.dequeue()
        return str(value)

    def peek(self):
        """peek"""
        value = self.my_list.peek()
        return str(value)

    def size(self):
        """size"""
        value = self.my_list.size()
        return str(value)

    def is_empty(self):
        """is empty"""
        value = self.my_list.is_empty()
        return str(value)

    def traverse(self):
        """traverse"""
        self.my_list.traverse()

    def menu(self):
        """menu"""
        while True:
            print("1) Lägg till värde")
            print("2) Ta bort nästa värde")
            print("3) Kolla på nästa värde")
            print("4) Storlek")
            print("5) Tom?")
            print("6) Show all items")
            print("q) Quit")

            choice = input("--> ")

            if choice == "q" or choice == "Q":
                print("\nExiting\n")
                break
            elif choice == "1":
                choice = input("Värde--> ")
                self.enqueue(choice)
            elif choice == "2":
                value = self.dequeue()
                print("Tog bort: " + value)
            elif choice == "3":
                value = self.peek()
                print("Peek: " + value)
            elif choice == "4":
                value = self.size()
                print("Size: " + value)
            elif choice == "5":
                value = self.is_empty()
                print("Tom? " + value)
            elif choice == "6":
                self.traverse()
            else:
                print("Please choose a valid option!")

if __name__ == '__main__':
    game = Handler()
