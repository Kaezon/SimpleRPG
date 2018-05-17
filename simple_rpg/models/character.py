"""Module containing the Character class"""
import re

from simple_rpg.enums import CHARACTER_STATE
from simple_rpg.orm.character import Character as ORMCharacter
from simple_rpg.orm.character_equipment import CharacterEquipment

INITIAL_MONEY = 25
INITIAL_HEALTH = 15
INITIAL_MANA = 10


class Character(object):
    """Character model."""
    def __init__(self, bot, owner_id):
        self.owner_id = owner_id
        self.bot = bot
        self.model = None
        self.state = CHARACTER_STATE.IDLE

        self.load_or_initialize()

    @property
    def max_health(self):
        """
        Get character's max health value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        self.model.health_max

    @property
    def max_mana(self):
        """
        Get character's max mana value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        self.model.mana_max

    @property
    def strength(self):
        """
        Get character's strength value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        strength = self.model.strength
        for value in [self.bot.items[item.id_string].stat_modifiers.strength
                      for item in self.model.equipment.list_equipment()
                      if item is not None]:
            strength += value
        return strength

    @property
    def defense(self):
        """
        Get character's defense value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        defense = self.model.defense
        for value in [self.bot.items[item.id_string].stat_modifiers.defense
                      for item in self.model.equipment.list_equipment()
                      if item is not None]:
            defense += value
        return defense

    @property
    def agility(self):
        """
        Get character's agility value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        agility = self.model.agility
        for value in [self.bot.items[item.id_string].stat_modifiers.agility
                      for item in self.model.equipment.list_equipment()
                      if item is not None]:
            agility += value
        return agility

    @property
    def dexterity(self):
        """
        Get character's dexterity value.

        This will include modifications by buffs, debuffs, and equipment.

        Returns:
            int: The caulated stat value.
        """
        dexterity = self.model.dexterity
        for value in [self.bot.items[item.id_string].stat_modifiers.dexterity
                      for item in self.model.equipment.list_equipment()
                      if item is not None]:
            dexterity += value
        return dexterity

    def load_or_initialize(self):
        """
        Load the character from the database if it exists; otherwise, run the
        character creation process.
        """
        record = self.bot.sql_connector.get_character(self.owner_id)
        if record is not None:
            self.model = record
            self.load_character()
            self.bot.characters[self.owner_id] = self
        else:
            self.model = ORMCharacter(owner_id=self.owner_id)

    def get_item(self, item: str):
        """
        Return an inventory record, or None if the character doesn't have any.
        """
        for inventory in self.model.inventory:
            if inventory.item.id_string == item:
                return inventory
        return None

    def get_member(self, ctx):
        """Return the owner member object for this character."""
        return ctx.guild.get_member(self.owner_id)

    def equip(self, equip_slot, item_record):
        """Equip an item."""

        if equip_slot == 'head':
            self.model.equipment.head = item_record.item
        elif equip_slot == 'body':
            self.model.equipment.body = item_record.item
        elif equip_slot == 'left_hand':
            self.model.equipment.left_hand = item_record.item
        elif equip_slot == 'right_hand':
            self.model.equipment.right_hand = item_record.item
        elif equip_slot == 'feet':
            self.model.equipment.feet = item_record.item
        # Handle "hands" special case
        else:
            raise Exception("Equip failed?")

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
                "Say `done` when you are ready to move on, or `cancel` to "
                "stop this process without creating a character.\n"
                .format(
                    unassigned=self.model.skill_points,
                    strength=self.model.strength,
                    defense=self.model.defense,
                    agility=self.model.agility,
                    dexterity=self.model.dexterity))
            message = await ctx.bot.wait_for(
                'message',
                check=lambda m: m.channel == m.author.dm_channel)
            split_message = str.split(message.content)

            # Process message
            if split_message[0] == 'assign':
                if len(split_message) != 3:
                    await ctx.send("Expected 3 arguments!")
                    continue

                if split_message[1].lower() in ['str', 'def', 'agl', 'dex']:
                    # Prevent using more SP than the character has
                    if (int(split_message[2]) > self.model.skill_points):
                        await ctx.send(
                            "You don't have that many skill points!")
                    # Make sure there is an integer to process
                    elif re.search('\d+', split_message[2]):
                        # Assign points to the selected character stat
                        if split_message[1].lower() == 'str':
                            if (int(split_message[2]) +
                                    self.model.strength < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.model.strength += int(split_message[2])
                            self.model.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'def':
                            if (int(split_message[2]) +
                                    self.model.defense < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.model.defense += int(split_message[2])
                            self.model.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'agl':
                            if (int(split_message[2]) +
                                    self.model.agility < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.model.agility += int(split_message[2])
                            self.model.skill_points -= int(split_message[2])

                        if split_message[1].lower() == 'dex':
                            if (int(split_message[2]) +
                                    self.model.dexterity < 0):
                                await ctx.send(
                                    "You cannot lower your stats below 0!")
                                break
                            self.model.dexterity += int(split_message[2])
                            self.model.skill_points -= int(split_message[2])

            # Stop looping if done
            if split_message[0] == 'done':
                break
            # Return if the command is cancel
            if split_message[0] == 'cancel':
                await ctx.send('Canceling character creation.')
                return

        self.model.equipment = CharacterEquipment()
        self.model.money = INITIAL_MONEY
        self.model.health_max = INITIAL_HEALTH
        self.model.health = INITIAL_HEALTH
        self.model.mana_max = INITIAL_MANA
        self.model.mana = INITIAL_MANA

        self.bot.sql_connector.add_new_character(self.model)
        self.bot.sql_connector.session.commit()

        self.bot.characters[ctx.message.author.id] = self

        await ctx.send("Your character has been created and saved.")
