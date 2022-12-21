#!/usr/bin/python3

import MySQLdb
import sys
if (len(sys.argv) > 1):

    conn = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    data = conn.cursor()
    data.execute("SELECT * FROM states")
    result = data.fetchall()

    for state in result:
        print(state, end="\n")
