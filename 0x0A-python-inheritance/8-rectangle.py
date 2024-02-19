#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """geometry"""

    def area(self):
        """Raise an exception massage"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """rectangle class inherited form basegeometry"""

    def __init__(self, width, height):
        """initialize rectangle instance

        Args:
            width (int): private positive integer
            height (int): private positve integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

