#!/usr/bin/python3

"""urllib module test"""

import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t - type: {type} \n\t - content: {res} \n\t - utf8 content: {content}".format(
            type=type(response.read()), res=the_page, content=the_page.decode()))
