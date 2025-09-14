#!/usr/bin/python3
"""
This module defines a function `say_my_name`.

The function prints "My name is <first_name> <last_name>".
It validates that first_name and last_name are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): First name.
        last_name (str): Last name (optional).

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
