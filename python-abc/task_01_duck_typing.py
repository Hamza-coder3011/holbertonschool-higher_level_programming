#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi as hw


class Shape(ABC):
    """Abstract base class for geometric shapes"""

    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return hw.pi * self.radius ** 2

    def perimeter(self):
        return 2 * hw.pi * self.radius
    
    def __str__(self):
        return f"Circle(area={self.area():.2f}, perimeter={self.perimeter():.2f})"


class Rectangle(Shape):
    """Rectangle shape class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle(area={self.area():.2f}, perimeter={self.perimeter():.2f})"


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
