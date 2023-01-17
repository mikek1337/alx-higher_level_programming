#!/usr/bin/python3

"""Github auth."""

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import sys
    import requests
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
