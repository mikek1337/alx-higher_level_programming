#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""Module class for squares"""

class Square(Rectangle):
    """module square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
