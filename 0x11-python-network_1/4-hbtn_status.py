#!/usr/bin/python3

"""using request."""

if __name__ == "__main__":
    import requests
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {type}\n\t- content: {content}".format(
        type=type(response.text), content=response.text))
