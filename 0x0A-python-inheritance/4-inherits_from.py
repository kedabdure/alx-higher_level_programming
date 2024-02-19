#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """check if the object is inherited form a class

     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj an object is inherited from specified class - True.
        Otherwise - False.
    """
    return isinstance(obj, type) and (issubclass(type(obj), a_class))
