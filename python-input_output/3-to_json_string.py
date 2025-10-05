#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (as a string).

    Args:
        my_obj: The Python object to serialize into a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    # Use json.dumps() to convert the Python object to a JSON-formatted string.
    # No need to handle exceptions if the object can't be serialized.
    return json.dumps(my_obj)
