"""Module containing the SQLAlchemy database connecter"""
import hashlib
import json
import logging

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from .orm import ORMBase
from .orm.character import Character
from .orm.character_inventory import CharacterInventory
from .orm.item import Item
from .schematics import ItemSchematic


logger = logging.getLogger('simple_rpg')


class SQLConnecter:
    def __init__(self, engine):
        self.engine = engine
        self.sessionmaker = (sessionmaker(bind=self.engine))
        self._session = None

    @property
    def session(self):
        if self._session is None:
            self._session = self.sessionmaker()
        return self._session

    def add_item(self, item: ItemSchematic):
        """Add an item to the database."""
        item_hash = hashlib.sha256(
            json.dumps(item.to_primitive()).encode('utf-8')).hexdigest()
        self.session.add(Item(id_string=item.identifier, item_hash=item_hash))
        self.session.commit()

    def add_item_to_character(self, character_id, item_id, quantity):
        """Add an item to a character's inventory."""
        inventory_record = self.session.query(CharacterInventory) \
            .filter(and_(CharacterInventory.character_id == character_id,
                         CharacterInventory.item_id == item_id)) \
            .one_or_none()
        if inventory_record is None:
            inventory_record = CharacterInventory(
                character_id=character_id,
                item_id=item_id,
                quantity=0)
            self.session.add(inventory_record)
        inventory_record.quantity += quantity
        self.session.commit()

    def initialize_database(self):
        """Creates all of the tables and populates the static tables"""
        ORMBase.metadata.create_all(self.engine, checkfirst=True)
        # TODO: Static Tables

    def get_character(self, member_id):
        """
        Selects a character record from the database with the given owner_id
        """
        return self.session.query(Character) \
            .filter(Character.owner_id == member_id).one_or_none()

    def get_all_items(self):
        """Selects all items from the item table."""
        return self.session.query(Item).all()

    def get_item(self, item_identifier):
        """Get an item with the given identifier string."""
        return self.session.query(Item) \
            .filter(Item.id_string == item_identifier).one_or_none()

    def add_new_character(self, character_record):
        """Add a character record to the database"""
        self.session.add(character_record)
        self.session.commit()

    def get_character_inventory(self, character_id):
        """Get all inventory records related to this character"""
        return self.session.query(CharacterInventory) \
            .filter(CharacterInventory.character_id == character_id).all()

    def remove_item_from_character(self, character_id, item_id, quantity):
        """Remove a quantity of an item from a character's inventory."""
        inventory_record = self.session.query(CharacterInventory) \
            .filter(and_(CharacterInventory.character_id == character_id,
                         CharacterInventory.item_id == item_id)) \
            .one_or_none()
        if inventory_record is None:
            logger.warning(
                "Tried to remove {quantity} of {item_id} from character_id "
                "{character_id}, but there was no record!"
                .format(quantity=quantity,
                        item_id=item_id,
                        character_id=character_id))
        elif inventory_record.quantity > quantity:
            logger.warning(
                "Tried to remove {quantity} of {item_id} from character_id "
                "{character_id}, but they only had {inventory_quantity}!"
                .format(quantity=quantity,
                        item_id=item_id,
                        character_id=character_id,
                        inventory_quantity=inventory_record.quantity))
        elif inventory_record.quantity == quantity:
            self.session.delete(inventory_record)
        else:
            inventory_record.quantity -= quantity
            self.session.commit()

    def update_items(self, items: list):
        """
        Update Item table with new and modified objects.
        args:
            items: A list of ItemScematic objects.
        """
        for item in items:
            item_hash = hashlib.sha256(
                json.dumps(item.to_primitive()).encode('utf-8')).hexdigest()
            item_record = self.session.query(Item) \
                .filter(Item.id_string == item.identifier).one_or_none()
            if item_record is None:
                self.add_item(item)
            elif item_record.item_hash != item_hash:
                logger.warning("Detected change to item: {}"
                               .format(item.identifier))
                item_record.item_hash = item_hash
                self.session.commit()
