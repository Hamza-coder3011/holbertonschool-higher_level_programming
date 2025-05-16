#!/usr/bin/python3
"""
This module provides a function that prints text with indentation.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
