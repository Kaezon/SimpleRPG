"""Module containing the SQLAlchemy model for character inventories"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from . import ORMBase


class CharacterInventory(ORMBase):
    """
    Model representing an item and the quantity of the item in a character's
    inventory.
    Fields:
      - 
    """
    __tablename__ = 'character_inventory'

    id = Column(
        Integer, Sequence('character_inventory_id_seq'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    quantity = Column(Integer)

    character = relationship("Character", back_populates="inventory")
