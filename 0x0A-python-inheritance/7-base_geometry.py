#!/usr/bin/python3

"""Module for base geometry class hope this explains needs more"""




class BaseGeometry:
    """Base class for geometry hope this explains needs more """
    def area(self):
        """unimplemented area method this doc exists"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validate if value is an integer or not"""
        if(not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
    