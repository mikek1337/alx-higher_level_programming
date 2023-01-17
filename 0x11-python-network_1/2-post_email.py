#!/usr/bin/python3

"""Send POST request with data."""

if __name__ == "__main__":
    import urllib.request
    import sys
    data = {"email": sys.argv[2]}
    data = str(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(
        sys.argv[1], data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content)
