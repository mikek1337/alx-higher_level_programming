#!/usr/bin/python3

"""Module base"""


class Base:
    """Base class to be inherited by all"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initalize id by value provided or by object count"""
        self.id = id
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
