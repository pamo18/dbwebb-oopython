#!/usr/bin/env python3

"""
Main
"""
from unorderedlist import UnorderedList

class Handler:
    """
    Handler
    """
    def __init__(self):
        """init"""
        self.my_list = UnorderedList()
        self.menu()

    def is_empty(self):
        """empty"""
        value = self.my_list.is_empty()
        return value

    def add(self, choice):
        """add"""
        self.my_list.add(choice)

    def insert(self, index, data):
        """insert"""
        self.my_list.insert(index, data)

    def set(self, index, data):
        """set"""
        self.my_list.set(index, data)

    def size(self):
        """size"""
        value = self.my_list.size()
        return value

    def get(self, index):
        """get"""
        value = self.my_list.get(index)
        return value

    def index_of(self, value):
        """index of"""
        position = self.my_list.index_of(value)
        return position

    def print_list(self):
        """print list"""
        self.my_list.print_list()

    def remove(self, item):
        """remove"""
        self.my_list.remove(item)

    def is_found(self, value):
        """is found"""
        return self.my_list.is_found(value)

    def menu(self):
        """menu"""
        while True:
            print("1) Empty?")
            print("2) Add")
            print("3) Insert")
            print("4) Set")
            print("5) Size")
            print("6) Get")
            print("7) Index of")
            print("8) Print list")
            print("9) Remove")
            print("q) Quit")

            choice = input("--> ")

            if choice == "q" or choice == "Q":
                print("\nExiting\n")
                break

            elif choice == "1":
                value = self.is_empty()
                print("Tom? " + str(value))

            elif choice == "2":
                choice = input("Value--> ")
                self.add(choice)
                print("Added: " + choice)

            elif choice == "3":
                choice_pos = input("Position--> ")
                choice_val = input("Insert--> ")

                self.insert(choice_pos, choice_val)

            elif choice == "4":
                choice_pos = input("Position--> ")
                choice_val = input("Set--> ")

                self.set(choice_pos, choice_val)

            elif choice == "5":
                value = self.size()
                print("Size: " + str(value))

            elif choice == "6":
                choice = input("Index--> ")

                self.get(choice)

            elif choice == "7":
                choice = input("Value--> ")
                position = self.index_of(choice)
                print("Has position: " + str(position))

            elif choice == "8":
                self.print_list()

            elif choice == "9":
                choice = input("Remove--> ")

                self.remove(choice)

            else:
                print("Please choose a valid option!")





if __name__ == '__main__':
    game = Handler()
