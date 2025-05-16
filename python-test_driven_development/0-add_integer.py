#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

def add_integer(a, b=98):
    """Adds two integers or floats (casted to integers).

    Args:
        a: First number (int or float).
        b: Second number (int or float), default is 98.
    
    Returns:
        The sum of a and b after casting to integers.

    Raises:
        TypError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(100.3, -2)
    98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
