#!/usr/bin/python3
def safe_print_integer(value):
    try:
        return value.isdigit()
    except AttributeError:
        return False
