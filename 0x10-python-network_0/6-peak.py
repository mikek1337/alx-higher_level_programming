#!/usr/bin/python3

def find_peak(list_of_integer):
    """Find the peak number from a list."""
    if len(list_of_integer) > 0:
        list_of_integer.sort()
        return list_of_integer[len(list_of_integer) - 1]
