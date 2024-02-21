#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file

    Args:
        filename (str): file name to be read
    """

    with open("my_file_0.txt") as f:
        f.read()
