#!/usr/bin/env python3
"""
Module for serializing and deserializing a custom Python object using pickle.
"""

import pickle
import os


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize this instance to a file using pickle.

        Parameters:
            filename (str): Path of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            # Handle file errors or pickling errors
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize an object from a file using pickle.

        Parameters:
            filename (str): Path of the file containing the serialized object.

        Returns:
            CustomObject or None: Returns the deserialized object,
            or None if error occurs.
        """
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.UnpicklingError):
            return None
