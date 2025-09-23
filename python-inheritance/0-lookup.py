#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the attributes and methods of the object.
    """
    return dir(obj)
