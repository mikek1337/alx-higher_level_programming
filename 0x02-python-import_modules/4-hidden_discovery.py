#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    dirnames = dir(hidden_4)
    for dirname in dirnames:
        if dirname[:2] != "__":
            print(dirname)