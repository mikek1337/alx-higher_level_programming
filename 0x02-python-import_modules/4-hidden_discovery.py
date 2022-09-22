#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    
    dirnames = dir(hidden_4)
    for dirname in dirnames:
        if dirname[:2] != "__":
            print(dirname)
