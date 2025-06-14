#!/usr/bin/python3
"""
Module that defines a function to save a Python object to a file
using JSON format"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to serialize and write.
        filename (str): The name of the file where to save the JSON string.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
