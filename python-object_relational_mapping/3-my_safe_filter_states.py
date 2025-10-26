#!/usr/bin/python3
"""
Lists all values in the states table where name matches the argument.
This version is safe from MySQL injections.
"""

import sys
import MySQLdb


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> "
              "<mysql_password> <database_name> <state_name>")
        sys.exit(1)


    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()


    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))


    rows = cur.fetchall()
    for row in rows:
        print(row)


    cur.close()
    db.close()
