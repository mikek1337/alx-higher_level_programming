#!/usr/bin/python3

"""Module to determine inherts"""

def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class