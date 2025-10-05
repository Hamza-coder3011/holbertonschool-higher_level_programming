#!/usr/bin/env python3
"""
Module to convert a CSV file into a JSON file using serialization.
"""

import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert the contents of a CSV file into JSON and save it to data.json.

    Parameters:
        csv_filename (str): Path to the CSV file to read.

    Returns:
        bool: True if conversion was successful, False if an error occurred.
    """
    try:
        # Read CSV file and convert each row to a dictionary
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Serialize list of dictionaries to JSON
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        # Catch any other exceptions (e.g., permission errors)
        return False
