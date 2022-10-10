#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    count = 0
    res = []
    while count < list_length:
        try:
            res.append((my_list_1[count] / my_list_2[count]))
            count += 1
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
            count += 1
        except TypeError:
            print("wrong type")
            res.append(0)
            count += 1
        except IndexError:
            print("out of range")
            res.append(0)
            count += 1
    return res
