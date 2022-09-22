#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    arglen = len(argv) - 1
    argsum = 0
    while arglen > 0:
        argsum += int(argv[arglen])
        arglen -= 1
    print(argsum)
