#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arglen = len(sys.argv) - 1
    argv = sys.argv
    count = 1
    if arglen == 0:
        print("{len} arguments.".format(len=arglen))
    elif arglen == 1:
        print("{len} argument.".format(len=arglen))
        print("{len}: {arg}".format(len=arglen, arg=argv[1]))
    else:
        print("{len} arguments:".format(len=arglen))
        while count <= arglen:
            print("{count}: {arg}".format(count=count, arg=argv[count]))
            count += 1
