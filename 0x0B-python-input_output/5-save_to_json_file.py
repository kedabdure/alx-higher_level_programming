#!/usr/bin/python3
"""save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """return json representation of an object"""
    
    serializable_list = list(my_obj)
    with open(filename, "w") as f:
        """save data to the json file"""

        return json.dump(serializable_list, f)
