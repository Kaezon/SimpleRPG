"""Decorators for use with SimpleRPG"""
from discord.ext import commands

from ..exceptions import HasNoCharacterException


def has_character():
    def predicate(ctx):
        if ctx.bot.get_or_load_character(ctx.message.author.id):
            return True
        else:
            raise HasNoCharacterException
    return commands.check(predicate)
