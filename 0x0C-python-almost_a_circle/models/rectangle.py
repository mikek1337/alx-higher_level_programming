#!/usr/bin/python3

"""Module Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value"""
        self.handleError("width", value)
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.handleError("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.handleError("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.handleError("y", value)
        self.__y = value

    def area(self):
        return self.width * self.height

    def handleError(self, name, value):

        if type(value) != int:
            raise TypeError("{} must be integer".format(name))

        if value < 0:
            raise ValueError("{} must be > 0".format(name))

    def display(self):
        for i in range(self.height):
            if (i + 1) >= self.height:
                for j in range(self.width):
                            print("#", end="")
            print("")