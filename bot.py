"""Module containing the Discord bot functionality."""

from os import getenv, path
import traceback

from discord.ext import commands
from sqlalchemy import create_engine

from simple_rpg import cogs, exceptions
from simple_rpg.item_processor import ItemProcessor
from simple_rpg.models.character import Character
from simple_rpg.sql_connector import SQLConnecter
from simple_rpg.util.yaml import load_items

COMMAND_PREFIX = '!'
item_dir = path.join(path.dirname(path.realpath(__file__)), 'items')


class RPGBot(commands.Bot):
    """A derivitive of the standard Discord bot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pm_help=True, **kwargs)
        self.characters = {}
        self.items = {}

        self.item_processor = ItemProcessor(self)

        for item in load_items(item_dir):
            self.items[item.identifier] = item

        self.sql_connector = SQLConnecter(create_engine('sqlite://'))

        self.add_cog(cogs.admin.Admin(self))
        self.add_cog(cogs.characters.Characters(self))
        self.sql_connector.initialize_database()
        self.sql_connector.update_items(self.items.values())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_command_error(self, ctx, error):
        if isinstance(error, exceptions.HasNoCharacterException):
            await ctx.send('You must create a character first!')
        else:
            ctx.send('An error occured!')
            print("Error - {}: {}".format(type(error).__name__, error))
            print(traceback.print_tb(error.__traceback__))

    def get_or_load_character(self, member_id: str):
        """
        Get the character associated with a Discord ID.
        args:
            member_id: A Discord UID.
        returns:
            Character or None
        """

        if member_id in self.characters:
            return self.characters[member_id]

        # Check for record in database
        character_record = self.sql_connector.get_character(member_id)
        if character_record is not None:
            self.characters[member_id] = Character(owner_id=member_id)
            return self.characters[member_id]

        return None


if __name__ == '__main__':
    bot = RPGBot(command_prefix=COMMAND_PREFIX)
    bot.run(getenv('DISCORD_TOKEN'))
