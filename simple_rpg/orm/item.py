"""Module containing the SQLAlchemy model for items"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from . import ORMBase


class Item(ORMBase):
    __tablename__ = 'items'

    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    id_string = Column(String)
