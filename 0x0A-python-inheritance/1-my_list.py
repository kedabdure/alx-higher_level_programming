#!/usr/bin/python3
"""my list"""


class MyList(list):
    """subclass of list"""

    def print_sorted(self):
        """print the sorted list"""
        sorted_list = sorted(self)

        print (sorted_list)
