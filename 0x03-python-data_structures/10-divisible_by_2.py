#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisable = []
    for i in my_list:
        if i % 2 == 0:
            divisable.append(True)
        else:
            divisable.append(False)
    return divisable
