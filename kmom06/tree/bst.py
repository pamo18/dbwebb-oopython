#!/usr/bin/env python3
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# pylint: disable=no-else-return

"""
Binary Search Tree, bst
"""

from node import Node

class BinarySearchTree:
    """
    Binary Search Tree, bst
    """
    def __init__(self):
        """init"""
        self.root = None

    def insert(self, key, value):
        """insert"""
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)

    @staticmethod
    def _insert(key, value, node):
        """insert recursive function"""
        if node.__gt__(key):
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif node.__lt__(key):
            if node.has_right_child():
                BinarySearchTree._insert(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value

    def inorder_traversal_print(self):
        """in order print"""
        if self.root is None:
            return None
        else:
            self._print_nodes(self.root)

    @staticmethod
    def _print_nodes(node):
        """recursive in order print"""
        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)
        print(node.value)
        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)

    def get(self, key):
        """get"""
        found = self._get(key, self.root)
        if found is None:
            raise KeyError
        else:
            return found.value

    @staticmethod
    def _get(key, node):
        """get recursive function"""
        if node.__eq__(key):
            return node
        elif node.__gt__(key):
            if node.has_left_child():
                return BinarySearchTree._get(key, node.left)
        elif node.__lt__(key):
            if node.has_right_child():
                return BinarySearchTree._get(key, node.right)
        else:
            return None

    def remove(self, key):
        """remove"""
        if self.root is None:
            #There is no tree
            raise KeyError
        elif self.get(key) is None:
            #The key is not found
            raise KeyError
        elif self.root.key == key and self.root.is_leaf():
            #Key found is root of tree and tree has no children, it is a leaf
            val = self.root.value
            self.root = None
        elif self.root.key == key and self.root.has_both_children():
            #Key found is root of tree and tree has both left and right children
            val = self.root.value
            temp = self._find_lowest(self.root.right)
            temp.left = self.root.left
            self.root = self.root.right
        else:
            #There is a tree, key is in tree, tree root is not the key
            val = self._remove(key, self.root)
        return val

    @staticmethod
    def _find_lowest(node):
        """find lowest key"""
        if node.is_leaf():
            return node
        else:
            return BinarySearchTree._find_lowest(node.left)

    @staticmethod
    def _remove(key, node):
        """remove recursive function"""
        if node.__gt__(key):
            #key not found recursive function for left side of tree
            return BinarySearchTree._remove(key, node.left)

        elif node.__lt__(key):
            #key not found recursive function for right side of tree
            return BinarySearchTree._remove(key, node.right)

        elif node.__eq__(key):
            #key to remove is found
            val = node.value
            #if node.has_parent():
                #found node is a child
            if node.has_parent() and node.is_left_child():
                #found node is a left child
                if node.has_left_child() and not node.has_right_child():
                    #found node only has left child
                    node.parent.left = node.left
                elif node.has_right_child() and not node.has_left_child():
                    #found node only has right child
                    node.parent.left = node.right
                elif node.has_both_children():
                    #found node has left and right child
                    temp = BinarySearchTree._find_lowest(node.right)
                    temp.left = node.left
                    node.parent.left = node.right
                elif node.is_leaf():
                    #found node has no children and is a leaf
                    node.parent.left = None

            elif node.has_parent() and node.is_right_child():
                #found node is a right child
                if node.has_left_child() and not node.has_right_child():
                    #found node only has left child
                    node.parent.right = node.left
                elif node.has_right_child() and not node.has_left_child():
                    #found node only has right child
                    node.parent.right = node.right
                elif node.has_both_children():
                    #found node has left and right child
                    temp = BinarySearchTree._find_lowest(node.right)
                    temp.left = node.left
                    node.parent.right = node.right
                elif node.is_leaf():
                    #found node has no children and is a leaf
                    node.parent.right = None
            #return the found node value
            return val
