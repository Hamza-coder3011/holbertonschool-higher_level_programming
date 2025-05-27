#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry will serve as a base class for geometry-related operations.
    """
    def area(self):
        """
        This method should be implemented by subclasses.
        Raises:
            Exception: always, with a message indicating
            the method is not implemented.
        """
        raise Exception("area() is not implemented")
