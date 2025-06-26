#!/usr/bin/python3
"""Defines State class mapped to the states table via SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance Base à utiliser pour l'héritage
Base = declarative_base()


class State(Base):
    """State class mapped to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
