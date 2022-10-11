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

    def my_print(self):
        """Print the square in hash is size is not zero"""
        total_size = self.__size
        count = 0
        if (total_size == 0):
            print(' ')
        while count < total_size:
            j = 0
            while j < total_size:
                print("#", end="")
                j += 1
            print('')
            count += 1
