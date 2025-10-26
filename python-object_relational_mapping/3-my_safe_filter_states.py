#!/usr/bin/python3
"""
Safe script that lists all rows in the `states` table of a given
database where `name` matches the provided argument.

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password> \
<database_name> <state_name>
"""

import MySQLdb
import sys


def main(argv):
    if len(argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password>"
              "<database_name> <state_name>".format(argv[0]))

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = None
    cursor = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=db_name
        )

        cursor = db.cursor()

        query = (
            "SELECT * FROM states WHERE name = %s "
            "ORDER BY id ASC"
            )
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("MySQL Error:", err)
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


if __name__ == "__main":
    main(sys.argv)
