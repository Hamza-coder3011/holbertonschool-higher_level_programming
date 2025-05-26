#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""


class MyList(list):
    """
    MyList inherits from list and provides a method to print
    the list sorted in ascending order without modifying the original list.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
