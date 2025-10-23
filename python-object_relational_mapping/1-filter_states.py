#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username  MySQL username
    mysql_password  MySQL password
    database_name   Database containing the 'states' table

Functionality:
    - Connects to a MySQL server on localhost at port 3306
    - Retrieves states whose names start with 'N'
    - Results are sorted by states.id in ascending order
    - Prints each state row as a tuple (id, name)

Requirements:
    - Python3
    - MySQLdb module (install via 'pip3 install mysqlclient')
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
