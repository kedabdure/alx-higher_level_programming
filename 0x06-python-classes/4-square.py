#!/usr/bin/python3
"""defining the class square."""


class Square:
    """representing the square"""

    def __init__(self, size=0):
        """defining the methode

        Args:
            size (int) represent the size of the square.
        """
        self.__size = size

    def area(self):
        """Return the current area"""

        return self.__size * self.__size

    @property
    def size(self):
        """return the value of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """modify the original value"""

        self.__size = value
