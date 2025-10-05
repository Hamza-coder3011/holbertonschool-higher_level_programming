#!/usr/bin/python3
"""
This module contains a function class_to_json(obj) that returns
the dictionary representation of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization (only simple data types).

    Args:
        obj: an instance of a Class

    Returns:
        dict: a dictionary containing serializable attributes
              (lists, dictionaries, strings, integers, booleans)
    """
    # __dict__ stores all instance attributes of an object
    return obj.__dict__
