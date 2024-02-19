#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """check if the object is an instance of class

     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
