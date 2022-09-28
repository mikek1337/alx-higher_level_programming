#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        new_list.append(i)
        if (i == search):
            idx = new_list.index(i)
            new_list[idx] = replace

    return new_list
