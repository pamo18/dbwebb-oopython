#!/usr/bin/env python3
# pylint: disable=no-else-return

"""
Main
"""
from trie import Trie

class SpellChecker:
    """
    SpellChecker class
    """
    def __init__(self):
        """init"""
        self.trie = Trie()
        self.word_list = "frequency.txt"
        self.web_words = ""

    def new_trie(self):
        """Create new Trie object"""
        self.trie = Trie()

    def change_wordlist(self, word_list):
        """Change word list"""
        self.new_trie()
        self.word_list = word_list
        self.add_words()

    def get_web_words(self):
        """get words for web view"""
        return self.web_words

    def get_word_list(self):
        """get current words list"""
        return self.word_list

    def add_words(self):
        """Add words"""
        try:
            with open(self.word_list, "r") as filehandle:
                lines = filehandle.read()
                words = lines.splitlines()
                for word in words:
                    self.trie.add(word)
        except FileNotFoundError:
            print("Invalid filename, try again or type reset!\n")
            print("What dictionary do you want to use?")
            user = input("--> ")
            if user.lower() == "quit" or user.lower() == "reset":
                self.word_list = "frequency.txt"
                self.add_words()
                print("\nReseting...")
            else:
                self.change_wordlist(user)

    def find_word(self, user):
        """Is the word spelled correctly"""
        result = self.trie.search(user)
        if __name__ == '__main__':
            if result:
                print("\n" + user + " is in the list and spelled correctly!")
            else:
                print("\n" + user + " is not in the list.")
        return result

    def prefix_search(self, user):
        """Print top ten words with highest frequency and prefix"""
        first_run = True
        user_next = ""

        while True:
            if first_run:
                user_search = user
                first_run = False
            else:
                user = user_search
                user_next = input("Enter another letter or quit to exit: " + \
                user)
                user_search = user + user_next
            if user.lower() == "quit" or user_next.lower() == "quit":
                break
            else:
                results = self.trie.print_prefix_words(user_search)

                if isinstance(results, list):
                    sorted_results = self.merge_sort(results, True)
                    for n in sorted_results[0:10]:
                        print(n)
                elif isinstance(results, str):
                    print(results)
                else:
                    print("\nNo words found")
                    break

    def print_word_list(self):
        """Print all words sorted by merge sort"""
        results = self.trie.print_words()
        if results:
            sorted_results = self.merge_sort(results)
            if __name__ == '__main__':
                for n in sorted_results:
                    print(n)
                print("\nThere are " + str(len(results)) + " words in the list")
                print("\nThe words have also been merge sorted!")
        return sorted_results

    def merge_sort(self, word_list, freq=False):
        """Merge sort part 1"""
        if len(word_list) <= 1:
            return word_list
        else:
            middle = len(word_list) // 2
            left = self.merge_sort(word_list[:middle], freq)
            right = self.merge_sort(word_list[middle:], freq)
            merge_sorted = self._merge_sort(left, right, freq)
            return merge_sorted

    @staticmethod
    def _merge_sort(left, right, freq):
        """Merge sort part 2"""
        sorted_list = []
        word_freq = False
        l = 0
        r = 0

        while l < len(left) and r < len(right):
            if len(left[l].split()) == 2 and freq:
                word_freq = True
                left_val = left[l].split()[1]
                right_val = right[r].split()[1]
            else:
                left_val = left[l].split()[0]
                right_val = right[r].split()[0]
            if word_freq:
                if float(left_val) > float(right_val):
                    sorted_list.append(left[l])
                    l += 1
                else:
                    sorted_list.append(right[r])
                    r += 1
            else:
                if left_val < right_val:
                    sorted_list.append(left[l])
                    l += 1
                else:
                    sorted_list.append(right[r])
                    r += 1

        sorted_list += left[l:] + right[r:]
        return sorted_list

    def make_web_list(self):
        """Make string of words or table data for web view"""
        word_list = self.print_word_list()
        if len(word_list[0].split()) == 2:
            word_str = "<table><tr><th>Word</th><th>Frequency</th></tr>"
            for word in word_list:
                word_str += "<tr><td>" + word.split()[0] +\
                "</td><td>" + word.split()[1] + "</td></tr>"
            word_str += "</table>"
        else:
            word_str = "<p>"
            for word in word_list:
                word_str += word + ", "
            word_str += "</p>"
        self.web_words = word_str

    def menu(self):
        """menu"""
        while True:
            print("\n1) Check a word")
            print("2) Get word suggestion")
            print("3) Change dictionary")
            print("4) Print all words in sorted order")
            print("q) Quit")

            choice = input("--> ")

            if choice.lower() == "q" or choice.lower() == "quit":
                print("\nExiting\n")
                break

            elif choice == "1":
                print("Type the word to check its spelling!")
                user = input("--> ")
                self.find_word(user)

            elif choice == "2":
                print("Type three letters, enter, then one letter at a time")
                user = input("--> ")

                while len(user) < 3:
                    print("You must type three letters, try again!")
                    user = input("--> ")
                self.prefix_search(user)

            elif choice == "3":
                print("What dictionary do you want to use?")
                user = input("--> ")
                self.change_wordlist(user)

            elif choice == "4":
                print("Here are all the words!\n")
                self.print_word_list()

            else:
                print("\nPlease choose a valid option!")


if __name__ == '__main__':
    sc = SpellChecker()
    sc.add_words()
    sc.menu()
