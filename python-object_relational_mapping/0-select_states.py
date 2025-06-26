#!/usr/bin/python3
"""
Script that lists all states from the database.
Takes 3 arguments: mysql username, mysql password, and database name.
Connect to a MySQL server running on localhost at part 3306.
Results are sorted in ascending order by states.id.
"""


import MySQLdb
import sys


if __name__ == "__main":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
