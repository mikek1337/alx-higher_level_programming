#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self) -> int:
        """Return the area of the retangle"""
        return (self.height * self.width)

    def perimeter(self) -> int:
        """Return the perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return (0)
        return (2*(self.height + self.width))

    def __str__(self) -> str:
        """prints rectangle using width and height with # character"""
        rect = []
        if self.width == 0 or self.height == 0:
            return ("")
        for i in range(0, self.height):
            for j in range(0, self.width):
                rect.append(str(self.print_symbol))
            if i == self.height - 1:
                return "".join(rect)
            rect.append("\n")

    def __repr__(self) -> str:
        rep = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return rep

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
