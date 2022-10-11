#!/usr/bin/python3
"""Square class"""


class Square:
    '''Represent square'''

    def __init__(self, size=0):
        """
        Initialize square
        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        '''Returns size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Set size of the square

            Args:
                size (int): The size of the new square
        '''
        if (type(value) is not int):
            raise TypeError("size must be integer")
        elif (value < 0):
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        '''Calculate the area of the square'''
        return (self.__size * self.__size)
