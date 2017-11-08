"""Module containing the Discord bot functionality."""

import asyncio
from os import getenv

import discord
from discord.enums import ChannelType
from discord.ext import commands

import cogs

COMMAND_PREFIX = '!'


class RPGBot(commands.Bot):
    """A derivitive of the standard Discord bot"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pm_help=True, **kwargs)
        self.characters = {}

        self.add_cog(cogs.characters.Characters(self))

    async def on_ready():
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


if __name__ == '__main__':
    bot = RPGBot(command_prefix=COMMAND_PREFIX)
    bot.run(getenv('DISCORD_TOKEN'))
