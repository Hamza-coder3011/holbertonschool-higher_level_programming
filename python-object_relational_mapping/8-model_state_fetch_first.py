#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Création de la connexion à la base de données
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db_name}", pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer uniquement le premier State trié par id
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    session.close()
