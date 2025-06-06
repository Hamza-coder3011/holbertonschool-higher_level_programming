#!/usr/bin/python3
"""
Module that defines a function to read and print
the content of a UTF-8 text file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
