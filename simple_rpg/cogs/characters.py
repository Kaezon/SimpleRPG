import logging

import discord
from discord.ext import commands

from ..models.character import Character
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
        if ctx.message.author.id in self.bot.characters:
            await ctx.send('You already have a character!')
        else:
            if not isinstance(ctx.channel, discord.DMChannel):
                message = await ctx.send(
                    "You will be DM'd shortly to begin the character "
                    "creation process.")
                ctx.channel = message.channel

            character = Character(ctx.bot, ctx.message.author.id)
            await character.create(ctx)
