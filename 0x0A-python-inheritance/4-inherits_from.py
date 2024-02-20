#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """check if the object is inherited form a class

     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
