#!/usr/bin/python3
"""List all cities."""
import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) > 1:
        conn = MySQLdb.connect(
            "localhost", sys.argv[1], sys.argv[2], sys.argv[3])
        data = conn.cursor()
        data.execute(
            "SELECT cities.id ,cities.name, states.name FROM cities INNER JOIN states on states.id = cities.state_id ORDER BY cities.id")
        result = data.fetchall()
        for city in result:
            print(city)
