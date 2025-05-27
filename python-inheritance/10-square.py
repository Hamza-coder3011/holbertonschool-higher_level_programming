#!/usr/bin/python3
"""Module that defines a class Square inheriting from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a Square
        Args:
            size (int): the size of the square's sides
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
