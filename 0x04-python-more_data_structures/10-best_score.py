#!/usr/bin/python3

def best_score(a_dictionary):
    big_score = 0
    key = ''
    if a_dictionary == None:
        return None
    for i, v in a_dictionary.items():
        if v > big_score:
            big_score = v
            key = i
    return key
