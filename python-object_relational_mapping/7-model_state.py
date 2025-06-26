#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and bind it
    url = f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db_name}"
    engine = create_engine(url, pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
