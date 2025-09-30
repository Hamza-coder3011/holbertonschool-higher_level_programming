#!/usr/bin/python3
"""
This module provides a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    Args:
    filename (str): Name of the file to write to.
    text (str): The string content to write.

    Returns:
    int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
