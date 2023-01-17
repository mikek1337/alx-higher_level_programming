#!/usr/bin/python3

"""Exception manage in urilib."""

if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        urllib.error.HTTPError(sys.argv[1])
