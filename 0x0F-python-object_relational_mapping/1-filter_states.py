#!/usr/bin/python3
"""Filter states with N as initial."""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
    data = conn.cursor()
    data.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    result = data.fetchall()

    for state in result:
        print(state, end="\n")
