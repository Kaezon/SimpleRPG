"""Module containing the SQLAlchemy model for character equipment"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from . import ORMBase


class CharacterEquipment(ORMBase):
    __tablename__ = 'character_equipment'

    id = Column(
        Integer, Sequence('character_equipment_id_seq'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    head = Column(Integer, ForeignKey('item.id'))
    body = Column(Integer, ForeignKey('item.id'))
    left_hand = Column(Integer, ForeignKey('item.id'))
    right_hand = Column(Integer, ForeignKey('item.id'))
    feet = Column(Integer, ForeignKey('item.id'))

    character = relationship("Character", back_populates="equipment")
