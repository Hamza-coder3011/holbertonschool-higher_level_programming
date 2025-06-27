#!/usr/bin/python3
"""
Script to look for the MySQL server state with a given name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = None
    cursor = None

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print("({}, '{}')".format(state[0], state[1]))

    cursor.close()
    db.close()
