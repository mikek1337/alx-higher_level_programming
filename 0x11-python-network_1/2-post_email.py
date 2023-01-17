#!/usr/bin/python3

"""Send POST request with data."""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data).encode("ascii")
    req = urllib.request.Request(
        sys.argv[1], data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content)
