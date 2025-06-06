#!/usr/bin/python3
"""
Provides a CustomObject class with serialization and deserialization
using the pickle module.
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to the given filename using pickle.

        Args:
            filename (str): The path to the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from the given filename.

        Args:
            filename (str): The path to the file to load the object from.

        Returns:
            CustomObject or None if an error occurred.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
