"""Module containing the Character class"""
import asyncio

from discord.ext import commands
import sqlalchemy

from simple_rpg.constants import CHARACTER_STATE, EQUIPMENT_DICT


class Character(object):
    def __init__(self, owner_id):
        self.owner_id = owner_id
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

    @commands.command()
    async def create_character(self, ctx):
        """
        Present the user with the character creation process and save the
        resulting stats to the database.
        """
        ctx.send("This would normally begin character creation.")

    def load_character(self):
        """Load the character stats from the database"""
        pass
