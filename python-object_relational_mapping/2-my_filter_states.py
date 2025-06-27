#!/usr/bin/python3
"""
Show the states of a DB MySQL with a specified name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupère les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connecte la base SQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )

    # Ouverture du curseur
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    query = query.format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))

    # Nettoyage
    cursor.close()
    db.close()
