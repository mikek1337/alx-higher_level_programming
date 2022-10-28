#!/usr/bin/python3

"""Module base"""

class Base:
    def __init__(self, id=None):
        self.__nb_objects = 0
        self.id = id
        if id == None:
            self.nb_objects =+ 1
        
    
    @property
    def nb_objects(self):
        return self.__nb_objects
    
    @nb_objects.setter
    def nb_objects(self, value):
        self.__nb_objects = value