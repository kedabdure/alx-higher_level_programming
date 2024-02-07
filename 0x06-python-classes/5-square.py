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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prtint the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
