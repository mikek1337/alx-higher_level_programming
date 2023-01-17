#!/usr/bin/python3

"""Get the X-Request-Id."""

if __name__ == "__main__":
    import sys
    import requests
    req = requests.get(sys.argv[1])
    print(req.headers["X-Request-Id"])
