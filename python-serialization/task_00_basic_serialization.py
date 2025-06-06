#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize an objet
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    A function that serialize a Python dictionary to a JSON file """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """
    A function that deserialize the JSON file to recreate the Python
    Dictionary """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)