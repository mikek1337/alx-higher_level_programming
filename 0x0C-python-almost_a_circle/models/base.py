#!/usr/bin/python3

"""Module base"""

from email.mime import base
import json


class Base:
    """Base class to be inherited by all"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initalize id by value provided or by object count"""
        self.id = id
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """String representation of a dictionary"""
        if list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts json string to object"""
        if json_string == None or json_string == "[]":
            return None
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the list object to file"""
        filename = cls.__name__+".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        if dictionary != None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Reads json file"""
        filename = cls.__name__+".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = Base.from_json_string(json_string)
                return [cls.create(**dic) for dic in dictionaries]
        except IOError:
            return []
