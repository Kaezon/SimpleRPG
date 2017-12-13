"""Module containing the SQLAlchemy model for items"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

import simple_rpg.orm as orm


class Item(orm.ORMBase):
    """
    This table is used to map items in character's persistent inventory
    records to object instances loaded into memory.
    Fields:
      - id<Integer>: Primary Key
      - id_string<String>: A unique string that will relate a record to an
                           object
      - item_hash<String>: A hash of the object, allowing the bot to detect
                           changes in objects between loads.
    """
    __tablename__ = 'items'

    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    id_string = Column(String, index=True, unique=True)
    item_hash = Column(String)
