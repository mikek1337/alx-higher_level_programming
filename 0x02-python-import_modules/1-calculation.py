#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{a} + {b} = {res}".format(a=a, b=b, res=add(a, b)))
    print("{a} - {b} = {res}".format(a=a, b=b, res=sub(a, b)))
    print("{a} * {b} = {res}".format(a=a, b=b, res=mul(a, b)))
    print("{a} / {b} = {res}".format(a=a, b=b, res=div(a, b)))
