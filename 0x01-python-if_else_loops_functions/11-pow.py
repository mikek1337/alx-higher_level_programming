#!/usr/bin/python3
def pow(a, b):
    i = 0;
    mul = 1
    if(b < 0):
        i = abs(b);
    while(i > 0):
        mul *= a
        i -= 1
    return mul