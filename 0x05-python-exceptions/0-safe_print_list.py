#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end='', sep='\n')
            count += 1
        except IndexError as err:
            print('')
            return count
    print('')
    return count
