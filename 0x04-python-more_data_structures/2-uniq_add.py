#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    i = 0
    sum = 0
    while i < len(my_list):
        count = i + 1
        while count < len(my_list) - 1:
            if my_list[count] == my_list[i]:
                my_list[count] = 0
            count += 1
        i += 1

    for i in my_list:
        sum += i

    return sum
