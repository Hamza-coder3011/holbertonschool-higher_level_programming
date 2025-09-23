#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList:
    """Custom list class that inherits from built-in list."""
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
