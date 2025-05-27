#!/usr/bin/python3
"""
This module defines an abstract class Animal
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """  An abstract class Shape """
    @abstractmethod
    def area(self):
        """
        Return the area of the Shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter of the Shape
        """
        pass


class Circle(Shape):
    """  A concrete class Circle inheritated from Shape """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Return the area of the Circle
        """
        return pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """
        Return the perimeter of the Circle
        """
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    """  A concrete class Rectangle inheritated from Shape """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the Rectangle
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
