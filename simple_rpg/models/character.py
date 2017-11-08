"""Module containing the Character class"""
import asyncio
import logging

import discord
from discord.ext import commands
import sqlalchemy

from simple_rpg.constants import CHARACTER_STATE, EQUIPMENT_DICT

logger = logging.getLogger('SimpleRPG')


class Character(object):
    def __init__(self, name):
        self.name = name
        self.state = CHARACTER_STATE.IDLE
        self.equipment = EQUIPMENT_DICT.copy()
        self.inventory = []
        self.money = 0

    def load_or_initialize(self):
        """
        Load the character from the database if it exists; otherwise, run the
        character creation process.
        """
        pass

    async def create_character(self):
        """
        Present the user with the character creation process and save the
        resulting stats to the database.
        """
        pass

    def load_character(self):
        """Load the character stats from the database"""
        pass
