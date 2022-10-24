#!/usr/bin/python3

"""Module to determine inherts in subclass"""

def inherits_from(obj, a_class):
    """to determine if it is the subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class