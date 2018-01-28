"""Module containing the SQLAlchemy model for character objects"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from . import ORMBase
from .character_inventory import CharacterInventory


class Character(ORMBase):
    __tablename__ = 'characters'

    def __init__(self, owner_id):
        self.owner_id = owner_id
        self.skill_points = 5
        self.money = 0
        self.health = 0
        self.health_max = 0
        self.mana = 0
        self.mana_max = 0
        self.strength = 0
        self.defense = 0
        self.agility = 0
        self.dexterity = 0


    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    owner_id = Column(String, index=True, nullable=False)
    skill_points = Column(Integer, default=0)
    equipment_id = Column(
        Integer, ForeignKey('character_equipment.id'), nullable=False)
    money = Column(Integer, default=0)
    health = Column(Integer, default=0)
    health_max = Column(Integer, default=0)
    mana = Column(Integer, default=0)
    mana_max = Column(Integer, default=0)
    strength = Column(Integer, default=0)
    defense = Column(Integer, default=0)
    agility = Column(Integer, default=0)
    dexterity = Column(Integer, default=0)

    inventory = relationship(
        "CharacterInventory",
        order_by=CharacterInventory.id,
        back_populates="character")

    equipment = relationship(
        "CharacterEquipment",
        primaryjoin="Character.equipment_id==CharacterEquipment.id")

    def __repr__(self):
        return ("<Character(id={character_id}, owner_id={owner_id})>")
