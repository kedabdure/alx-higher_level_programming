#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read file

    Args:
        filename (str): file name to be read
    """

    with open("my_file_0.txt", encoding="utf-8") as f:
        """file read as f form my_file_0.txt"""

        print(f.read(), end="")
