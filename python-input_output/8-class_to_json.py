#!/usr/bin/python3
"""
Function that returns the dictionary description for
JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.

    Args:
        obj: An instance of a class

    Returns:
        dict: A dictionary containing all serialization
            attributes of the object (list, dict,
            str, int, bool)
    """
    return obj.__dict__
