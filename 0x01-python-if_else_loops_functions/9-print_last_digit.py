#!/usr/bin/python3
def print_last_digit(number):
    negative = 0
    if (number < 0):
        number = number * -1
        mod = number % 10
    else:
        mod = number % 10

    print(mod, end='')
    return mod
