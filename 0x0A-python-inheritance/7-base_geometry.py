#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """geometry"""

    def area(self):
        """Raise an exception massage"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates and integer"""

        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
