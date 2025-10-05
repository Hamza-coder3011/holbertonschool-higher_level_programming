#!/usr/bin/python3
"""
This module defines a Student class with first_name,
last_name, and age attributes, and methods to_json(attrs=None)
for selective dictionary representation of a Student instance.
"""


class Student:
    """
    Defines a Student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                            If None or not a list, include all attributes.

        Returns:
            dict: Dictionary of selected or all attributes.
        """
        if isinstance(attrs, list):
            # Include only attributes that exist and are in attrs
            return {
                key: value for key,
                value in self.__dict__.items() if key in attrs
                }
        # If attrs is None or not a list, return all attributes
        return self.__dict__.copy()
