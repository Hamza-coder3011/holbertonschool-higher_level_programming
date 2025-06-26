#!/usr/bin/python3
'''Safely filters states by name using user input'''

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=pwd, db=db_name)

    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    for id, name in rows:
        print("({}, '{}')".format(id, name))

    cursor.close()
    db.close()
