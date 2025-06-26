#!/usr/bin/python3
"""Creates the table states in database using SQLAlchemy ORM"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Connexion au moteur MySQL avec SQLAlchemy
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Crée toutes les tables connues de Base
    Base.metadata.create_all(engine)
