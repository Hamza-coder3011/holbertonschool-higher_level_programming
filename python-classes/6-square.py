#!/usr/bin/python3
"""Defines a class Square with size and position attributes and print functionality."""


class Square:
    """Class that defines a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position (both validated via setters)."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size =value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position( self, value):
        """"Setter for position with type and content validation."""
        if(
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers.")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' and position offset."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
