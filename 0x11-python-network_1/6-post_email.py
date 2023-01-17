#!/usr/bin/python3

"""POST email to a given url"""

if __name__ == "__main__":
    import requests
    import sys
    data = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.text)
