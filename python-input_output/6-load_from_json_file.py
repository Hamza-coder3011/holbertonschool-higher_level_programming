#!/usr/bin/python3
"""Module to load a Python object from a JSON file."""


import json


def load_from_json_file(filename):
    """Load a Python object from JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
