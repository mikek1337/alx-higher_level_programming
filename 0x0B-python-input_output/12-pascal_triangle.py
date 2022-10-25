#!/usr/bin/python3

"""Pascal's triangle"""

def pascal_triangle(n):
    """"""
    if n <= 0:
        return []
    trilist = [[1]]
    for i in range(n):
        if len(trilist) == 2:
            trilist.append(1)
    
