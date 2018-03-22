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

    @commands.command()
    @checks.has_character()
    async def use(self, ctx, item: str, target: str):
        """Use an item from the character's inventory."""
        character = self.bot.get_or_load_character(
            ctx.message.author.id)
        if item not in self.bot.items:
            await ctx.send("There is no \"{}\"...").format(item)
            return

        inventory_record = character.get_item(item)
        if inventory_record is None:
            await ctx.send("You don't have any!")
            return

        item_schematic = self.bot.items[item]

        self.bot.item_processor.process_item(character, item_schematic)
        if inventory_record.quantity == 1:
            self.bot.sql_connector.session.delete(inventory_record)
        else:
            inventory_record.quantity -= 1

    @commands.command()
    @checks.has_character()
    async def status(self, ctx):
        """Get a readout of the character's stats."""
        character = self.bot.get_or_load_character(
            ctx.message.author.id)
        formatted_stats = (
            "===Kaezon's Stats===\n"
            "```HP: {health}/{health_max} MP: {mana}/{mana_max}```"
        ).format(
            health=character.model.health,
            health_max=character.model.health_max,
            mana=character.model.mana,
            mana_max=character.model.mana_max)
        await ctx.send(formatted_stats)
