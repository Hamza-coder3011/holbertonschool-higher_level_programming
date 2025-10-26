#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
