#!/usr/bin/python3

"""Module for student class"""


class Student:
    """Student representation object"""

    def __init__(self, first_name, last_name, age):
        """Initiates the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to get the dict of a class"""
        return self.__dict__
