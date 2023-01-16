#!/usr/bin/python3

def find_peak(list_of_integer):
    """Find the peak number from a list."""
    if list_of_integer is not None:
        sorted_list = list_of_integer.sort()
        return sorted_list[len(sorted_list) - 1]
