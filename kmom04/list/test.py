#!/usr/bin/env python3

"""
Test
"""

import unittest
from unorderedlist import UnorderedList

class Testlist(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def setUp(self):
        """ Create object for all tests """
        self.uol = UnorderedList()

    def tearDown(self):
        """ Remove dependencies after test """
        self.uol = None

    def test_add(self):
        """Test add"""
        self.uol.add("Test 1")
        self.assertEqual(self.uol.get("0"), "Test 1")

    def test_set(self):
        """Test set"""
        self.uol.add("1")
        self.uol.set("0", "Test 2")
        self.assertEqual(self.uol.get("0"), "Test 2")

    def test_get(self):
        """Test get"""
        self.uol.add("Test 3")
        self.assertEqual(self.uol.get("0"), "Test 3")

    def test_index_of(self):
        """Test index_of"""
        self.uol.add("Test")
        self.uol.add("ing")
        self.uol.add("Test 4")
        self.assertEqual(self.uol.index_of("Test 4"), 2)

    def test_remove(self):
        """Test remove"""
        self.uol.add("Test")
        self.uol.add("Test 5")
        self.uol.add("ing")
        self.uol.remove("Test 5")
        self.assertEqual(self.uol.index_of("Test 5"), "Not found!")
















if __name__ == '__main__':
    unittest.main(verbosity=3)
