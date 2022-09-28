#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = dict()
    new_dic = a_dictionary.copy()
    for i, v in new_dic.items():
        new_dic[i] = v * 2
    return new_dic
