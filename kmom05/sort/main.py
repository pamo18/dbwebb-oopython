#!/usr/bin/env python3
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
"""
Main
"""
from unorderedlist import UnorderedList
from sort import insertion_sort
from sort import insertion_sort_r
from sort import bubble_sort
from sort import bubble_sort_r

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
        to_insert = self.my_list.insert(index, data)
        return to_insert

    def set(self, index, data):
        """set"""
        confirm = self.my_list.set(index, data)
        return confirm

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
        to_remove = self.my_list.remove(item)
        return to_remove

    def is_found(self, value):
        """is found"""
        return self.my_list.is_found(value)

    def sort_list_ins(self):
        """sort insertion"""
        self.my_list = insertion_sort(self.my_list)

    def sort_list_ins_r(self):
        """sort insertion recursive"""
        self.my_list = insertion_sort_r(self.my_list)

    def sort_list_bub(self):
        """sort bubble"""
        self.my_list = bubble_sort(self.my_list)

    def sort_list_bub_r(self):
        """sort bubble recursion"""
        self.my_list = bubble_sort_r(self.my_list)

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
            print("10) Insertion sort")
            print("11) Recursive Insertion sort")
            print("12) Bubble sort")
            print("13) Recursive Bubble sort")
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
                if choice.isdigit():
                    choice = int(choice)
                self.add(choice)
                print("Added: " + str(choice))

            elif choice == "3":
                choice_pos = input("Position--> ")
                choice_val = input("Insert--> ")
                if choice_val.isdigit():
                    choice_val = int(choice_val)

                data = self.insert(choice_pos, choice_val)
                print("Inserted: " + str(data) + " into position " + choice_pos)

            elif choice == "4":
                choice_pos = input("Position--> ")
                choice_val = input("Set--> ")
                if choice_val.isdigit():
                    choice_val = int(choice_val)

                set_val = self.set(choice_pos, choice_val)
                try:
                    print("Set: " + str(set_val) + " at position " + choice_pos)
                except TypeError:
                    print("Failed")

            elif choice == "5":
                value = self.size()
                print("Size: " + str(value))

            elif choice == "6":
                choice = input("Index--> ")
                if choice.isdigit():
                    choice = int(choice)
                found = self.get(choice)

                try:
                    print("Found: " + str(found))
                except TypeError:
                    print("Found nothing!")

            elif choice == "7":
                choice = input("Value--> ")
                if choice.isdigit():
                    choice = int(choice)
                position = self.index_of(choice)
                print("Has position: " + str(position))

            elif choice == "8":
                self.print_list()

            elif choice == "9":
                choice = input("Remove--> ")
                if choice.isdigit():
                    choice = int(choice)

                item = self.remove(choice)
                print("Removed: " + str(item))

            elif choice == "10":
                self.sort_list_ins()
                self.print_list()

            elif choice == "11":
                self.sort_list_ins_r()
                self.print_list()

            elif choice == "12":
                self.sort_list_bub()
                self.print_list()

            elif choice == "13":
                self.sort_list_bub_r()
                self.print_list()

            else:
                print("Please choose a valid option!")





if __name__ == '__main__':
    game = Handler()
