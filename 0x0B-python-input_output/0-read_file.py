#!/usr/bin/python3

"""Module for file input"""


def read_file(filename=""):
    """Opens file in read mode"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
