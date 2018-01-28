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
        await ctx.send('I see you have a character.')

    @commands.command()
    async def create_character(self, ctx):
        if self.bot.get_or_load_character(ctx.message.author.id):
            await ctx.send('You already have a character!')
        else:
            if not isinstance(ctx.channel, discord.DMChannel):
                message = await ctx.send(
                    "You will be DM'd shortly to begin the character "
                    "creation process.")
                ctx.channel = message.channel

            character = Character(ctx.bot, ctx.message.author.id)
            await character.create(ctx)

    @commands.command()
    @checks.has_character()
    async def inventory(self, ctx):
        """Send the character's inventory to the channel"""
        character = self.bot.get_or_load_character(
            ctx.message.author.id)
        formatted_inventory = "==={}'s inventory===\n```\n".format(
            ctx.message.author.display_name)
        for inventory in character.model.inventory:
            formatted_inventory += "{item}: {quantity}\n".format(
                item=self.bot.items[inventory.item.id_string].display_name,
                quantity=inventory.quantity)
        formatted_inventory += "```"
        await ctx.send(formatted_inventory)
