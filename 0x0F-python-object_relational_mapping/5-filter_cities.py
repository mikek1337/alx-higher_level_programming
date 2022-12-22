#!/usr/bin/python3
"""List all cities with a given name"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) > 1:
        conn = MySQLdb.connect(
            "localhost", sys.argv[1], sys.argv[2], sys.argv[3])
        data = conn.cursor()
        data.execute(
            """SELECT cities.id ,cities.name, states.name FROM cities INNER JOIN states on states.id = cities.state_id WHERE states.name=%s ORDER BY cities.id""", (sys.argv[4],))
        result = data.fetchall()
        i = 0
        for state in result:
            print(state[1],end="")
            i+=1
            if len(result) > i:
                print(", ", end="") 
