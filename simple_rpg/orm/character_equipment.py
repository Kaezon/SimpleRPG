"""Module containing the SQLAlchemy model for character equipment"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

import simple_rpg.orm as orm


class CharacterEquipment(orm.ORMBase):
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
    head_item_id = Column(Integer, ForeignKey('items.id'))
    body_item_id = Column(Integer, ForeignKey('items.id'))
    left_hand_item_id = Column(Integer, ForeignKey('items.id'))
    right_hand_item_id = Column(Integer, ForeignKey('items.id'))
    feet_item_id = Column(Integer, ForeignKey('items.id'))

    head = relationship(
        "Item", primaryjoin="CharacterEquipment.head_item_id==Item.id")
    body = relationship(
        "Item", primaryjoin="CharacterEquipment.body_item_id==Item.id")
    left_hand = relationship(
        "Item", primaryjoin="CharacterEquipment.left_hand_item_id==Item.id")
    right_hand = relationship(
        "Item", primaryjoin="CharacterEquipment.right_hand_item_id==Item.id")
    feet = relationship(
        "Item", primaryjoin="CharacterEquipment.feet_item_id==Item.id")
