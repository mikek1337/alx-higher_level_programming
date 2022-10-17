#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Return the area of the retangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """
        Return the perimeter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return (0)
        return (2*(self.height + self.width))

    def __str__(self):
        """
        prints rectangle using width and height with # character
        """
        rect = []
        if self.width == 0 or self.height == 0:
            return ("")
        for i in range(0, self.height):
            for j in range(0, self.width):
                rect.append("#")
            rect.append("\n")
        return "".join(rect)
