#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_ele = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common_ele.append(i)
    return common_ele
