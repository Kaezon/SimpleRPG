"""Module containing the SQLAlchemy model for character equipment"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from . import ORMBase


class CharacterEquipment(ORMBase):
    """
    A model of a character's equip slots.
    Fields:
     - id<Integer>: Primary Key
     - character_id<Integer>: The id of the owning character record
     - head<Integer>: The id of the item eqiped to the character's head
     - body<Integer>: The id of the item eqiped to the character's body
     - left_hand<Integer>: The id of the item eqiped to the character's left
                           hand
     - right_hand<Integer>: The id of the item eqiped to the character's right
                            hand
     - feet<Integer>: The id of the item eqiped to the character's fet
    """
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
