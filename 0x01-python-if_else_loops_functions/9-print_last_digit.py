#!/usr/bin/python3
def print_last_digit(number):
    negative = 0
    if (number < 0):
        negative = number * -1
        mod = negative % 10
        mod = mod * -1
        return mod
    else:
        mod = number % 10

    print(mod, end='')
    return mod
