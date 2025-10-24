#!/usr/bin/python3
"""
Displays all values in the 'states' table of 'hbtn_0e_0_usa'
where 'name' matches the argument provided.

Usage:
    ./2-my_filter_states.py <mysql_username>
    <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username  MySQL username
    mysql_password  MySQL password
    database_name   Database containing the 'states' table
    state_name      State name to search for (case-sensitive)

Functionality:
    - Connects to a MySQL server on localhost at port 3306
    - Uses a SQL query formatted with the user input
    - Retrieves rows where the state name matches exactly
    - Results are sorted by id in ascending order
    - Prints each row as a tuple (id, name)

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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states WHERE name LIKE BINARY %s "
        "ORDER BY id ASC"
    )
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
