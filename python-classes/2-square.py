#!/usr/bin/python3
"""Defines a class Square with validated size attribute"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size: The size of the square (optional, default is 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integre")
        if size < 0:
            raise ValueError("size must be >= ")
        self.__size = size
