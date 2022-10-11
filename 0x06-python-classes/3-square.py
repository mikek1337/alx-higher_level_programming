#!/usr/bin/python3
"""Modeule square class"""


class Square:
    '''Represent square'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Return the area of the current size"""
        return self.__size * self.__size
