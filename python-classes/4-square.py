#!/usr/bin/python3
"""Defines a class Square with size property and area method"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new square using the setter to ensure validation"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
