#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """A class that inherits from the built-in list class."""

    def print_sorted(self):
        """
        Public instance method that prints the list, 
        but sorted in ascending order.
        """
        print(sorted(self))
