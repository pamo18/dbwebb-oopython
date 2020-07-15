#!/usr/bin/env python3

"""
Errors
"""

class Error(Exception):
    """User defined class for custom exceptions"""
    pass

class EmptyList(Error):
    """Raised when the list is empty"""
    pass

class CantFind(Error):
    """Raised when value not found in the list"""
    pass

class IndexTooHigh(Error):
    """Raised when position index is too high"""
    pass

class IndexTooLow(Error):
    """Raised when position index is too low"""
    pass

class NumbersOnly(Error):
    """Only numbers allowed"""
    pass
