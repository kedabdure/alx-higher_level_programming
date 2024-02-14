#!/usr/bin/python3
"""
calculate the sum of the two number
"""


def add_integer(a, b=98):
    """
    Return the sum of two number

    Args:
        a (int): first number.
        b (int): second number.

    Raises:
        TypeError: if a or b arn't intiger or float number

    Return:
        int: the sum of a and b.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
