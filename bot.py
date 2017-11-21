"""Module containing the Discord bot functionality."""

import asyncio
from os import getenv

from discord.ext import commands

from simple_rpg import cogs, exceptions

COMMAND_PREFIX = '!'


class RPGBot(commands.Bot):
    """A derivitive of the standard Discord bot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pm_help=True, **kwargs)
        self.characters = {}

        self.add_cog(cogs.characters.Characters(self))

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
