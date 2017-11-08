import logging

import discord
from discord.ext import commands

from discord.decorators import must_have_character

logger = logging.getLogger('SimpleRPG')


class Characters(object):
    def __init__(self, bot):
        self.bot = bot

    @must_have_character()
    @commands.command()
    async def character_test(self):
        logger.info("The function executed!")