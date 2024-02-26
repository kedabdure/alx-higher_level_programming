#!/usr/bin/python3
"""rectangle module"""

from base import Base

class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation of rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: optional variable
            y: optional varable
            id: the number of instance created
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """update width"""
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @property
    def x(self):
        """returns x"""
        return self.__x

    @property
    def y(self):
        """returns y"""
        return self.__y

    @height.setter
    def height(self, value):
        """update width"""
        self.__height = value

    @x.setter
    def x(self, value):
        """update width"""
        self.__x = value

    @y.setter
    def y(self, value):
        """update width"""
        self.__y = value
