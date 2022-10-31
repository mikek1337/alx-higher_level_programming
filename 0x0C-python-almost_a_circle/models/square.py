#!/usr/bin/python3

"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size to the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the value of the attributes"""
        i = 0
        vars = ["id", "size", "_Rectangle__x", "_Rectangle__y"]
        while i < len(args):
            if vars[i] == "size":
                self.size = args[i]
            else:
                self.__dict__[vars[i]] = args[i]
            i += 1

        for key, arg in kwargs.items():
            if key == "id":
                self.id = arg
            elif key == "size":
                self.size = arg
            else:
                self.__dict__['_Rectangle__'+key] = arg

    def to_dictionary(self):
        """Converts square attributes to dictionary representation"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
