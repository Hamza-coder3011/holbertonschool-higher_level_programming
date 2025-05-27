#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initializes a Square
        Args:
            size (int): the size of the square's sides
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
