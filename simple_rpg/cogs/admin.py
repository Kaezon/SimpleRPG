"""
This module contains the admin commands for SimeRPG.
"""
import logging

import discord
from discord.ext import commands

from .util.data import MemberConverter, NumberConverter


class Admin(object):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def give_item(self, ctx, item: str, num: NumberConverter,
                        *members: MemberConverter):
        """Give a character some quantity of an item."""
        item_record = self.bot.sql_connector.get_item(item)

        if item_record is None:
            await ctx.send("There is no \"{}\" item!".format(item))
            return

        for member in members:
            character_record = self.bot.sql_connector.get_character(
                member.id)
            if character_record is None:
                await ctx.send("{} does not have a character."
                               .format(member.display_name))
                return
            self.bot.sql_connector.add_item_to_character(
                character_id=character_record.id,
                item_id=item_record.id,
                quantity=num)
            await ctx.send(
                "Gave {quantity} of item {item} to {character}"
                .format(quantity=num,
                        item=item,
                        character=member.display_name))

    @commands.command()
    async def list_items(self, ctx):
        """List all items in the database."""
        item_records = self.bot.sql_connector.get_all_items()
        formatted_item_list = "===Items===\n```\n"
        for record in item_records:
            formatted_item_list += "{}\n".format(record.id_string)
        formatted_item_list += "```"

        await ctx.send(formatted_item_list)
