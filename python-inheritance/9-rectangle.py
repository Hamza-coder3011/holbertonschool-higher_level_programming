#!/usr/bin/python3
#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
         """Return the area of the rectangle"""
         return self.__width * self.__height
    
    def __str__(self):
        """Return string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
