#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)


    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()


    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
