#!/usr/bin/python3
"""file_append module"""


def append_write(filename="", text=""):
    """append to a file

    Args:
        filename (str): file name to write on
        text (str): text to write on file
    """

    with open(filename, "a", encoding="utf-8") as f:
        """append text to the end of the file"""

        return (f.write(text))
