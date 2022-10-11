#!/usr/bin/python3

class Square:
    '''Represent square'''

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be integer")
        if (size < 0):
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Return the area of the current size"""
        return self.__size * self.__size
