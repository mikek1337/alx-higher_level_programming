#!/usr/bin/python3

"""Module for file input output function how long does this\
    comment has to be"""


def read_file(filename=""):
    """Opens file in read mode and do nothing i guess really \
        long hope this passes"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
