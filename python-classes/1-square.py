#!/usr/bin/python3
"""Defines a class Square with a private size attribute"""


class Square:
    """Class that defines a square"""

    def __init__(self, size):
        """Initialize a newsquare

        Args:
            size: The size of square
        """
        self.__size = size
