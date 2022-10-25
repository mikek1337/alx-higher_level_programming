#!/usr/bin/python3

"""Module to write string to file"""

def write_file(filename="", text=""):
    """function to write to file"""
    with open(filename, "w", encoding="utf-8") as f:
       return f.write(text)