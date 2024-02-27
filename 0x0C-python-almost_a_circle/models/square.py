#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size: The size of the square
            x: Optional x-coordinate
            y: Optional y-coordinate
            id: The id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Update the class Squar by overriding the __str__ method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
