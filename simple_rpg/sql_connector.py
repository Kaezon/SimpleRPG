"""Module containing the SQLAlchemy database connecter"""
from sqlalchemy.orm import sessionmaker

from .orm import ORMBase
from .orm.character import Character


class SQLConnecter:
    def __init__(self, engine):
        self.engine = engine
        self.sessionmaker = (sessionmaker(bind=self.engine))
        self._session = None

    @property
    def session(self):
        if self._session is None:
            self._session = self.sessionmaker()
        return self._session

    def initialize_database(self):
        """Creates all of the tables and populates the static tables"""
        ORMBase.metadata.create_all(self.engine, checkfirst=True)

    def get_character(self, member_id):
        """
        Selects a character record from the database with the given owner_id
        """
        return self.session.query(
            Character).filter(Character.owner_id == member_id).one_or_none()

    def add_new_character(self, character_record):
        """Add a character record to the database"""
        self.session.add(character_record)
        self.session.commit()

    def update_static_tables(self):
        """Updates all of the static tables with new and modified objects"""
        pass
