#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    count = 0;
    for i in matrix:
        count = 0
        for j in i:
            print("{:d}".format(j), end='')
            if count != (len(i) - 1):
                print("{i}".format(i=' '), end="")
            count += 1
        print("")
