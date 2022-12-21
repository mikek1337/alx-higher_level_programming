#!/usr/bin/python3
"""Filter states with N as initial."""

import sys
import MySqlDB

if __name__ == "__main__":
    conn = MySqlDB.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    data = conn.cursor()
    data.execute("SELECT * FROM states WHERE name LIKE N% ORDER BY id")
    result = data.fetchall()

    for state in result:
        print(state, end="\n")
