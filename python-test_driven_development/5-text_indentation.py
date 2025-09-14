#!/usr/bin/python3
"""
This module defines a function `text_indentation`.

The function prints a text with 2 new lines after each
occurrence of '.', '?' or ':'. It trims leading and
trailing spaces from each printed line.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger new lines
    separators = ".?:"
    start = 0

    for idx, char in enumerate(text):
        if char in separators:
            # Slice from start to current character, strip spaces
            line = text[start:idx + 1].strip()
            print(line)
            print()
            start = idx + 1  # Start next slice after current char

    # Print any remaining text after the last separator
    remainder = text[start:].strip()
    if remainder:
        print(remainder)
