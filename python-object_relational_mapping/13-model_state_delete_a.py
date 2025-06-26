#!/usr/bin/python3
"""Deletes all State objects containing 'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to the database and deletes states containing 'a'."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer tous les State avec 'a' dans le nom
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
