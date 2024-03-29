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

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle class inherited form basegeometry"""

    def __init__(self, width, height):
        """initialize rectangle instance

        Args:
            width (int): private positive integer
            height (int): private positve integer
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of the rectangle"""

        return ("{}".format(self.__width * self.__height))

    def __str__(self):
        """print the width / height """
        string = "[{}] ".format(self.__class__.__name__)
        string += "{}/{}".format(self.__width, self.__height)

        return string


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
