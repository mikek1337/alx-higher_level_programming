#!/usr/bin/python3

"""Module for base geometry class hope this explains needs more"""


class BaseGeometry:
    """Base class for geometry hope this explains needs more """

    def __init__(self, width, height):
        """Initialize new rectangle"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        """unimplemented area method this doc exists"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is an integer or not"""
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
