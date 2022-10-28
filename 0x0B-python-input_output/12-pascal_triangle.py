#!/usr/bin/python3

"""
Module pascal triangle
"""


def pascal_triangle(n):
    """
    function pascal triangle
    """
    if n <= 0:
        return []
    trilist = [[1]]
    for i in range(n-1):
        j = 0
        tri = [1]
        while j < len(trilist[-1]):
            if j + 1 != len(trilist[-1]):
                tri.append(trilist[-1][j] + trilist[-1][j + 1])
            j = j + 1
        tri.append(1)
        trilist.append(tri)

    return trilist
