#!/usr/bin/python3

"""Handle error using request"""

if __name__ == "__main__":
    import requests
    import sys
    try:
        res = requests.get(sys.argv[1])
    except requests.HTTPError as e:
        print("Error code: {}".format(e.errno))
