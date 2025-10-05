#!/usr/bin/python3
"""CustomObject class with serialization and deserialization using pickle."""

import pickle


class CustomObject:
    """Defines a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serializes the current object to the specified file.

        Args:
            filename (str): Path to the output file.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            pass  # Silently fail as per instructions

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.

        Args:
            filename (str): Path to the input file.

        Returns:
            CustomObject | None: Deserialized object, or None on failure.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
