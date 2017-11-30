"""Module containing the SQLAlchemy model for character objects"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from . import ORMBase
from .character_inventory import CharacterInventory


class Character(ORMBase):
    __tablename__ = 'characters'

    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    owner_id = Column(String)
    skill_points = Column(Integer)
    equipment_id = Column(Integer, ForeignKey('character_equipment.id'))
    money = Column(Integer)
    health = Column(Integer)
    health_max = Column(Integer)
    mana = Column(Integer)
    mana_max = Column(Integer)
    strength = Column(Integer)
    defense = Column(Integer)
    agility = Column(Integer)
    dexterity = Column(Integer)

    inventory = relationship(
        "CharacterInventory",
        order_by=CharacterInventory.id,
        back_populates="character")

    equipment = relationship("CharacterEquipment", back_populates="character")

    def __repr__(self):
        return ("<Character(id={character_id}, owner_id={owner_id})>")
