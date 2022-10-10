#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as te:
        print("Exception: {:s}".format(te.args[0]))
        return False
