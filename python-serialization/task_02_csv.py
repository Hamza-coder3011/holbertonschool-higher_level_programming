#!/usr/bin/python3
"""
Converts a CSV file into a JSON file using serialization.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The path to the CSV file to convert.

    Returns:
        bool: True if successful, False if an error occurs.
    """
    try:
        with open(
            csv_filename,
            mode='r',
            newline='',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open(
            'data.json',
            mode='w',
            encoding='utf_8'
        ) as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False

    except Exception:
        return False
