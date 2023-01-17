#!/usr/bin/python3

"""Send request and get the header X-Request-Id."""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
