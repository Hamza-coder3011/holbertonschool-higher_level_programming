#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to serialize and save.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    # Open the file in write mode ("w")
    # Using 'with' ensures the file is properly closed after writing
    with open(filename, "w", encoding="utf-8") as f:
        # Use json.dump() to write the JSON representation
        # of the object directly into the file
        # No need to handle serialization or permission errors
        json.dump(my_obj, f)
