"""Module containing the SQLAlchemy database connecter"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import ORMBase


class SQLConnecter:
    def __init__(self, engine):
        self.engine = engine
        self._session = None

    @property
    def session(self):
        if self._session is None:
            self._session = sessionmaker(bind=self.engine)

    def initialize_database(self):
        """Creates all of the tables and populates the static tables"""
        ORMBase.metadata.create_all(self.engine)

    def update_static_tables(self):
        """Updates all of the static tables with new and modified objects"""
        pass
