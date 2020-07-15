#!/usr/bin/env python3

"""
Exceptions
"""

class Error(Exception):
    """User defined class for custom exceptions"""
    pass

class EmptyList(Error):
    """Raised when the list is empty"""
    pass
