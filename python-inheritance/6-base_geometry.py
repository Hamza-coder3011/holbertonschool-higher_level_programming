#!/usr/bin/python3
"""Module defining BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry shapes"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")
