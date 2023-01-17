#!/usr/bin/python3

"""Send POST request with data."""

if __name__ == "__main__":
    import urllib.request
    import sys
    req = urllib.request.Request(
        sys.argv[1], data={"email": sys.argv[2]}, method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
