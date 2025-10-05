#!/usr/bin/python3
"""Script that adds all command line arguments to a Python list,
and saves them to a file as a JSON representation.
"""

import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Name of the JSON file
filename = "add_item.json"

# If the file exists, load the existing list;
# otherwise start with an empty list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (except the script name itself)
items.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(items, filename)
