#!/usr/bin/python3
class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

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
        Retrieve a dictionary representation of the Student instance.

        If attrs is a list of str, only attributes with names in this
        list will be included. Otherwise, all public attributes are returned.

        Args:
            attrs (list, optional): A list of attribute names (str) to include.

        Returns:
            dict: A dictionary containing the selected attributes.
        """
        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        with values from a dictionary.

        Args:
            json (dict): A dictionary with keys as attribute names and
                        values as new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
