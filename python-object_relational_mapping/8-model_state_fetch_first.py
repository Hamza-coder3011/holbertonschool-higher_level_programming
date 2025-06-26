#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to the database and prints the first State object."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération du premier State trié par id (sans récupérer tous les résultats)
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main()
