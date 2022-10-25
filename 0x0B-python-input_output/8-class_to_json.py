#!/usr/bin/python3

"""Module class obj to list"""


def class_to_json(obj):
    """Function that returns methods and attributes of a class"""
    return obj.__dict__
