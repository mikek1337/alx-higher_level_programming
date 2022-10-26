#!/usr/bin/python3

"""Module to append data to file without destroying data"""


def append_write(filename="", text=""):
    """function to append text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
