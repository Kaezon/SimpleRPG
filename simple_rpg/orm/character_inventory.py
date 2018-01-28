"""Module containing the SQLAlchemy model for character inventories"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

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
    character_id = Column(
        Integer,
        ForeignKey('characters.id'),
        unique=True,
        index=True,
        nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    quantity = Column(Integer)

    character = relationship("Character", back_populates="inventory")
    item = relationship("Item")
