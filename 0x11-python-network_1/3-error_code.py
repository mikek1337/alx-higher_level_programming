#!/usr/bin/python3

"""Exception manage in urilib."""

if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
