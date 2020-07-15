#!/usr/bin/env python3

"""
Test
"""

import unittest
from node import Node
from trie import Trie
from spellchecker import SpellChecker

class TestNode(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.root = Node()

    def tearDown(self):
        """ Remove dependencies after test """
        self.root = None

    def test_add_child(self):
        """Node Test, add child"""
        letter1 = "t"
        letter2 = "w"
        new_node1 = Node(letter1)
        new_node2 = Node(letter2)
        self.root.add_child(letter1, new_node1)
        self.root.add_child(letter2, new_node2)
        self.assertEqual(self.root.children["t"].letter, "t")
        self.assertEqual(self.root.children["w"].letter, "w")
        self.assertTrue(len(self.root.children) == 2)

    def test_set_frequency(self):
        """Node Test, set and get frequency"""
        letter1 = "p"
        new_node1 = Node(letter1)
        self.root.add_child(letter1, new_node1)
        self.root.children["p"].set_frequency(10)
        self.assertEqual(self.root.children["p"].has_frequency(), 10)

    def test_set_complete(self):
        """Node Test, set and get complete word"""
        letter1 = "s"
        new_node1 = Node(letter1)
        self.root.add_child(letter1, new_node1)
        self.root.children["s"].set_complete()
        self.assertTrue(self.root.children["s"].is_complete())

class TestTrie(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.trie = Trie()

    def tearDown(self):
        """ Remove dependencies after test """
        self.trie = None

    def test_add(self):
        """Trie Test, add words"""
        word1 = "one 1"
        word2 = "two 2"
        self.trie.add(word1)
        self.trie.add(word2)
        self.assertTrue("one 1" in self.trie.print_words())
        self.assertTrue("two 2" in self.trie.print_words())

    def test_complete_word(self):
        """Trie Test, search with complete word marker"""
        word1 = "one 1"
        word2 = "two 2"
        self.trie.add(word1)
        self.trie.add(word2)
        self.assertTrue(self.trie.search("one"))
        self.assertTrue(self.trie.search("two"))

    def test_print_words(self):
        """Trie Test, print words"""
        word1 = "three 3"
        word2 = "four 4"
        self.trie.add(word1)
        self.trie.add(word2)
        self.assertTrue(self.trie.search("three"))
        self.assertTrue(self.trie.search("four"))

    def test_search_error(self):
        """Trie Test, search error wrong input"""
        word1 = "one 1"
        word2 = "two 2"
        self.trie.add(word1)
        self.trie.add(word2)
        with self.assertRaises(TypeError):
            self.assertTrue(self.trie.search(1))
            self.assertTrue(self.trie.search(2))

class TestSpellChecker(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.sc = SpellChecker()

    def tearDown(self):
        """ Remove dependencies after test """
        self.sc = None

    def test_change_dictionary(self):
        """Spellchecker Test, change dictionary"""
        dictionary = "tiny_frequency.txt"
        self.sc.change_wordlist(dictionary)
        self.assertEqual(self.sc.word_list, "tiny_frequency.txt")

    def test_merge_sort(self):
        """Spellchecker Test, merge sort"""
        test_list = ["four 4", "two 2", "one 1", "five 5", "three 3"]
        self.assertEqual(self.sc.merge_sort(test_list, True), \
        ["five 5", "four 4", "three 3", "two 2", "one 1"])

    def test_merge_sort_error(self):
        """Spellchecker Test, merge sort error"""
        test_list = ["4", 2, "1", 5, "3"]
        with self.assertRaises(AttributeError):
            self.assertEqual(self.sc.merge_sort(test_list, True), \
            ["5", "4", "3", "2", "1"])


if __name__ == '__main__':
    unittest.main(verbosity=3)
