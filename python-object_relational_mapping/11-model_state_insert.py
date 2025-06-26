#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Creates and adds 'Louisiana' state, then prints its id."""
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

    # Création de l'objet State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
