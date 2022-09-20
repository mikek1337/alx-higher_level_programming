#!/usr/bin/python3
def uppercase(str):
    uppercase = ''
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 123):
            uppercase += chr(ord(i) - 32)
        else:
            uppercase += i
    print("{x}".format(x=uppercase), end='\n')
