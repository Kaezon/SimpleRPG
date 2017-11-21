import logging

import discord
from discord.ext import commands

from ..util import checks

logger = logging.getLogger('SimpleRPG')


class Characters(object):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_character()
    async def character_test(self, ctx):
        character = self.bot.characters[ctx.message.author.id]
        await ctx.send('I see you have a character.')

    @commands.command()
    async def create_character(self, ctx):
        if ctx.message.author.id in bot.characters:
            await ctx.send('You already have a character!')
        else:
            if isinstance(ctx.channel, discord.DMChannel):
                await ctx.send(
                    "This would normally begin character creation... "
                    "but I'm lazy.")
            else:
                await ctx.send(
                    "You will be DM'd shortly to begin the character "
                    "creation process.")
                await ctx.message.author.send(
                    "This would normally begin character creation... "
                    "but I'm lazy.")
            self.bot.characters[ctx.message.author.id] = None
