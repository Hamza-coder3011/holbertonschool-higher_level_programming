#!/usr/bin/python3
"""Updates the name of the State with id=2 to 'New Mexico'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connects to the DB and updates State with id=2."""
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

    # Rechercher l'état avec id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Si trouvé, modifier le nom et sauvegarder
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
