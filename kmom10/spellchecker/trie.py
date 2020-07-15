#!/usr/bin/env python3
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=no-else-return
# pylint: disable=consider-using-enumerate
"""
Trie datastruktur
"""

from node import Node

class Trie:
    """
    Trie datastruktur
    """
    def __init__(self):
        """init"""
        self.root = Node()

    def add(self, list_word):
        """add word"""
        current = self.root
        if len(list_word.split()) == 2:
            split_word = list_word.split()
            word = split_word[0].lower()
            frequency = split_word[1]
        else:
            word = list_word.lower()
            frequency = False

        for i in range(len(word)):
            letter = word[i]
            if letter in current.children:
                current = current.children[letter]
            else:
                new_node = Node(letter)
                current.add_child(letter, new_node)
                current = current.children[letter]
        current.set_complete()
        if frequency:
            current.set_frequency(frequency)

    def search(self, find):
        """Search for word in list"""
        current = self.root
        found = False
        for l in find:
            if l in current.children:
                current = current.children[l]
            else:
                return found
        if current.is_complete():
            found = True

        return found

    def print_words(self):
        """Print words in list"""
        current = self.root.children
        word_list = []

        for c in current:
            words = self._print_words(current[c], word_list)

        return words

    @staticmethod
    def _print_words(node, word_list, word=""):
        """Print words in list"""
        word += node.letter
        if node.is_complete() and node.has_frequency():
            word_list.append(word + ' ' + node.has_frequency())
        elif node.is_complete():
            word_list.append(word)
        if node.children:
            for n in node.children:
                Trie._print_words(node.children[n], word_list, word)
        return word_list

    def print_prefix_words(self, prefix):
        """Print words witrh prefix"""
        current = self.root
        word_list = []
        word = ""
        for i in range(len(prefix)):
            if prefix[i] in current.children:
                current = current.children[prefix[i]]
                word += current.letter
            else:
                return
        if current.is_complete() and not current.children:
            if current.has_frequency():
                word_str = word + ' ' + current.has_frequency()
            else:
                word_str = word
            return word_str
        else:
            current = current.children

            for c in current:
                word_list = self._print_prefix_words(current[c],\
                prefix, word_list)

            return word_list

    @staticmethod
    def _print_prefix_words(node, prefix, word_list, word=""):
        """Print words witrh prefix"""
        word += node.letter
        if node.is_complete() and node.has_frequency():
            word_list.append(prefix + word + ' ' + node.has_frequency())
        elif node.is_complete():
            word_list.append(prefix + word)
        if node.children:
            for n in node.children:
                Trie._print_prefix_words(node.children[n], prefix,\
                word_list, word)
        return word_list
