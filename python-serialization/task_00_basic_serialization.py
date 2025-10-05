#!/usr/bin/env python3
"""
Basic serialization module to save/load Python dictionaries as JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The filename to save the JSON data to.
                        If the file exists, it will be replaced.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Parameters:
        filename (str): The JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
