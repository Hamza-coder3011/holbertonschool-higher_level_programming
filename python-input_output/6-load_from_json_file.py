#!/usr/bin/python3
"""
This module contains a function load_from_json_file(filename)
that reads a JSON file and returns the corresponding Python object.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON content.
    """
    # Open the file using the with statement
    # This ensures the file is properly closed after reading.
    with open(filename, "r", encoding="utf-8") as f:
        # Use json.load() to parse the file content into a Python object.
        # No need to handle exceptions for missing files or invalid JSON.
        return json.load(f)
