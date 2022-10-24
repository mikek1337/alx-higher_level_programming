#!/usr/bin/python3

"""Module to determine inherts in subclass am in hell"""


def inherits_from(obj, a_class):
    """to determine if it is the obj is subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
