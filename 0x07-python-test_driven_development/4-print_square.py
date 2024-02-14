#!/usr/bin/python3
"""print the square with the character #"""


def print_square(size):
    """print square with #
    
    Args:
        size (int): length of the square
    """
    
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    
    if size < 0:
        raise ValueError('size must be >= 0')
    
    for i in range(size):
        print("#" * size)
