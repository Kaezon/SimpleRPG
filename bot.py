"""Module containing the Discord bot functionality."""

import asyncio
from os import getenv, path

from discord.ext import commands
from sqlalchemy import create_engine

from simple_rpg import cogs, exceptions
from simple_rpg.sql_connector import SQLConnecter
from simple_rpg.util.yaml import load_items

COMMAND_PREFIX = '!'
item_dir = path.join(path.dirname(path.realpath(__file__)), 'items')


class RPGBot(commands.Bot):
    """A derivitive of the standard Discord bot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pm_help=True, **kwargs)
        self.characters = {}
        self.sql_connector = SQLConnecter(create_engine('sqlite://'))

        self.add_cog(cogs.characters.Characters(self))
        self.sql_connector.initialize_database()
        self.sql_connector.update_items(load_items(item_dir))

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


if __name__ == '__main__':
    bot = RPGBot(command_prefix=COMMAND_PREFIX)
    bot.run(getenv('DISCORD_TOKEN'))
