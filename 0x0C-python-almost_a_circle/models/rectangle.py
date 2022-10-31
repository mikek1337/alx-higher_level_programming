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
        """Prints rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")

        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates the value of the attributes"""
        i = 0
        vars = ["id", "_Rectangle__width", "_Rectangle__height", "_Rectangle__x", "_Rectangle__yy"]
        while i < len(args):
          
            self.__dict__[vars[i]] = args[i]
            i += 1

        for key, arg in kwargs.items():
            if key == "id":
                self.id = arg
            else:
                self.__dict__['_Rectangle__'+key] = arg
    
    def to_dictionary(self):
        """Converts object to dictionary representation"""
        return{
            "id":self.id,
            "width":self.width,
            "height":self.height,
            "x":self.x,
            "y":self.y
            }



