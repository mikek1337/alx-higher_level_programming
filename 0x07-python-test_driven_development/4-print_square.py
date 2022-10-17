#!/usr/bin/python3

"""
Module that prints squares
"""

def print_square(size):
    if not isinstance(size, int) or size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
         raise ValueError("size must be >=0")

    for i in range(0,size):
        for j in range(0, size):
            print("#", end='')
        print("")