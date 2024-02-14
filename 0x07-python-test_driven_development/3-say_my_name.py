#!/usr/bin/python3
"""Print the fullname"""

def say_my_name(first_name, last_name=""):
    """Print the first and the last name
    
    Args:
        first_name (string): first name
        last_name (string): last name
    """
    
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    
    print("My name is {} {}".format(first_name, last_name))
