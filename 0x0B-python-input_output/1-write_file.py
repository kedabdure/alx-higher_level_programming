#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write on file

    Args:
        filename (str): file name to write on
        text (str): text to write on file
    """
    with open(filename, "w", encoding="utf-8") as f:
        """function to write on the file"""

        return f.write(text)
