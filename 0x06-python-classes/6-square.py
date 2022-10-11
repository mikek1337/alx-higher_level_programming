#!/usr/bin/python3
"""Square class"""


class Square:
    '''Represent square'''

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square
        Args:
            size (int): The size of the new square
            position (tuple): (x, y) coordinates
        """
        self.size = size
        self.position = position

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
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def position(self):
        """Return positions tuple"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set positions"""
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
