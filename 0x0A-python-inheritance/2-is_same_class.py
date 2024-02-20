#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """check if the object is an instance of class"""

    if type(obj) is a_class:
        return True
    return False

