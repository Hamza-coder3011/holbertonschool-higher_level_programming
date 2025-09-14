#!/usr/bin/python3
"""
This module defines a function `print_square`.

The function prints a square with the character '#'.
It validates that size is a non-negative integer.
"""


def print_square(size):
    """
    Print a square of the given size using the '#' character.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    # Validate type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Validate value
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
