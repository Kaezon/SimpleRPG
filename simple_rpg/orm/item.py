"""Module containing the SQLAlchemy model for items"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from . import ORMBase


class Item(ORMBase):
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
    id_string = Column(String) # Make sure this is unique
    item_hash = Column(String)
