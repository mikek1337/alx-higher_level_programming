#!/usr/bin/python3

"""Module base"""

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

