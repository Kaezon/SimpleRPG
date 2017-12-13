"""Module containing the Character class"""
import asyncio
import re

from discord.ext import commands
import sqlalchemy

from simple_rpg.enums import CHARACTER_STATE, EQUIPMENT_DICT
from  simple_rpg.orm.character import Character as ORMCharacter


class Character(object):
    def __init__(self, bot, owner_id):
        self.owner_id = owner_id
        self.bot = bot
        self.model = None
        self.state = CHARACTER_STATE.IDLE
        self.skill_points = 5
        self.equipment = EQUIPMENT_DICT.copy()
        self.inventory = []
        self.money = 0
        self.health = 0
        self.health_max = 0
        self.mana = 0
        self.mana_max = 0
        self.strength = 0
        self.defense = 0
        self.agility = 0
        self.dexterity = 0

        self.load_or_initialize()

    def load_or_initialize(self):
        """
        Load the character from the database if it exists; otherwise, run the
        character creation process.
        """
        record = self.bot.sql_connector.get_character(self.owner_id)
        if record is not None:
            self.model = record
            self.bot.characters[self.owner_id] = self
        else:
            self.model = ORMCharacter(owner_id=self.owner_id)

    async def create(self, ctx):
        """
        Present the user with the character creation process and save the
        resulting stats to the database.
        """
        while True:
            await ctx.message.author.send(
                "You have {unassigned} uassigned skill points\n"
                "--------------------------------------------\n"
                "STR {strength}\n"
                "DEF {defense}\n"
                "AGL {agility}\n"
                "DEX {dexterity}\n"
                "--------------------------------------------\n"
                "Assign points with the following command:\n"
                "```assign {{str|def|agl|dex}} [integer]```\n"
                "Say `done` when you are ready to move on, or `cancel` to stop "
                "this process without creating a character.\n"
                .format(
                    unassigned=self.skill_points,
                    strength=self.strength,
                    defense=self.defense,
                    agility=self.agility,
                    dexterity=self.dexterity))
            message = await ctx.bot.wait_for(
                'message',
                check=lambda m: m.channel==m.author.dm_channel)
            split_message = str.split(message.content)

            # Process message
            if split_message[0] == 'assign':
                if len(split_message) != 3:
                    await ctx.send("Expected 3 arguments!")
                    continue

                if split_message[1] in ['str', 'def', 'agl', 'dex']:
                    # Prevent using more SP than the character has
                    if (int(split_message[2]) > self.skill_points):
                        await ctx.send("You don't have that many skill points!")
                    # Make sure there is an integer to process
                    elif re.search('\d+', split_message[2]):
                        # Assign points to the selected character stat
                        if split_message[1].lower() == 'str':
                            if (int(split_message[2]) + self.strength < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.strength += int(split_message[2])
                            self.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'def':
                            if (int(split_message[2]) + self.defense < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.defense += int(split_message[2])
                            self.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'agl':
                            if (int(split_message[2]) + self.agility < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.agility += int(split_message[2])
                            self.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'dex':
                            if (int(split_message[2]) + self.dexterity < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.dexterity += int(split_message[2])
                            self.skill_points -= int(split_message[2])

            # Stop looping if done
            if split_message[0] == 'done':
                break
            # Return if the command is cancel
            if split_message[0] == 'cancel':
                await ctx.send('Canceling character creation.')
                return

        self.model.owner_id = self.owner_id
        self.model.skill_points = self.skill_points
        self.model.equipment = None
        self.model.money = self.money
        self.model.health = self.health
        self.model.health_max = self.health_max
        self.model.mana = self.mana
        self.model.mana_max = self.mana_max
        self.model.strength = self.strength
        self.model.defense = self.defense
        self.model.agility = self.agility
        self.model.dexterity = self.dexterity
        self.bot.sql_connector.add_new_character(self.model)
        self.bot.characters[ctx.message.author.id] = self

        await ctx.send("Your character has been created and saved.")

    def load_character(self):
        """Load the character stats from the database"""
        pass

    def save_character(self):
        """Save this character to the database"""
        pass
