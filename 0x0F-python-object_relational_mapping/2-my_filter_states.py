#!/usr/bin/python3

"""Search by state name."""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="172.17.0.1", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=1234)
    data = conn.cursor()
    query = "SELECT * FROM states WHERE name={statename} ORDER BY id".format(
        statename='"'+sys.argv[4]+'"')
    data.execute(query)
    result = data.fetchall()

    for state in result:
        print(state, end="\n")
