#!/usr/bin/python3
"""Square class that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
