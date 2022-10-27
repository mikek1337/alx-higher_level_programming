#!/usr/bin/python3

"""Module base"""

class Base:
    def __init__(self, id=None):
        self.__nb_objects = 0
        if id != None:
            self.id = id
        
    
    @property
    def nb_objects(self):
        return self.__nb_objects
    
    @nb_objects.setter
    def nb_objects(self, value):
        self.__nb_objects = value
