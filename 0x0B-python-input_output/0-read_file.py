#!/usr/bin/python3

"""Module for file input output function"""


def read_file(filename=""):
    """Opens file in read mode and do nothing"""
    with open(filename, 'r',encoding="utf-8") as f:
        print(f.read(),end="")
