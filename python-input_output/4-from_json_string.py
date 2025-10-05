#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object (e.g., list, dict, etc.).
    """
    # Use json.loads() to convert a JSON-formatted string
    # into a native Python object (list, dict, int, str, etc.).
    # No need to handle exceptions if the string is invalid.
    return json.loads(my_str)
