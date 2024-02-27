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

    @property
    def size(self):
        """The width of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Setting the width of the square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update the class square"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """square to dict"""

        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
