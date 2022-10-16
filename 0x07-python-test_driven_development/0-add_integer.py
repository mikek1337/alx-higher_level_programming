#!/usr/bin/python3

"""
This is the add_integer module

This add_integer module supplies one function, add_integer(a, b). For example,

>>> add_integer(1, 1)
2
"""

def add_integer(a, b=98):
    """Returns the sum of two numbers
    >>> add_integer(1, 1)
    2
    >>> add_integer(1.0,1.1)
    1
    >>> add_integer('1',1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1,'1')
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    sum = 0
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum