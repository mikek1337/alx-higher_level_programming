#!/usr/bin/python3
"""
class for squares

Example:
    x = Square(1)
    python 0-main.py

Attributes:
    None

"""


class Square:
    """Represent square."""

    def __init__(self, size):
        """
        Initialize square
        Args:
            size (int): The size of the new square
        """
        self.__size = size
