#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor

        Args:
            size: the size of the squar
            x: optional arg
            y: optional arg
            id: the number of instance
        """
        super().__init__()
        super().__init__(size)
        self.size = Rectangle.width
        self.size = Rectangle.height

    def __str__(self):
        """Update the class Squar by overriding the __str__ method"""
        return "[Squar] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)
