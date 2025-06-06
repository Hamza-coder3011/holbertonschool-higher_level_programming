#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves the list to a file named 'add_item.json' using JSON format.

Behavior:
- If the file 'add_item.json' does not exist, it will be created.
- If the file exists, it will be loaded and the new arguments will be appended.
- The updated list is then saved back into the same file.

This script uses the following functions:
- save_to_json_file: saves a Python object as JSON to a file
- load_from_json_file: loads a Python object from a JSON file

Requirements:
- No need to handle file permission or exception errors.
- No external modules should be imported,
except the required user-defined functions.
"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"


if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
