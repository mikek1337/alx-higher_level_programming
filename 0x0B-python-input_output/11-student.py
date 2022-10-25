#!/usr/bin/python3

"""Module for student class"""


class Student:
    """Student representation object"""

    def __init__(self, first_name, last_name, age):
        """Initiates the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to get the dict of a class"""
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__[attrs]

    def reload_from_json(self, json):
        """function replace all attributes"""
        for k, v in json.items():
            setattr(self, k, v)
