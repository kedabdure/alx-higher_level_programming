#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """chsnge the dict to json"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """write to the file"""
        ob_dic = [obj.to_dictionary() for obj in list_objs]
        file_name = f"{cls.__name__}.json"
        js_str = cls.to_json_string(ob_dic)
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write([])
            else:
                f.write(js_str)
