#!/usr/bin/python3
class Student:
    """
    Defines a Student with first name, last name, and age,
    and provides JSON serialization/deserialization methods.
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
            # Include only attributes present in both attrs and the instance
            return {
                key: value for key,
                value in self.__dict__.items() if key in attrs
                }
        # Return all attributes if attrs is None or not a list
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary with key/value pairs to
            update the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
