#!/usr/bin/env python3
"""
Module for serializing and deserializing a Python dictionary to/from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML filename to save the data to.
    """

    root = ET.Element("data")

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string

    # Create an ElementTree and write it to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename: str) -> dict:
    """
    Deserialize an XML file into a Python dictionary.

    Parameters:
        filename (str): The XML filename to read.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text  # Keep values as strings
        return data_dict
    except (ET.ParseError, FileNotFoundError):
        return {}  # Return empty dictionary on error
