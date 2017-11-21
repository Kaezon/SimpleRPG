"""Decorators for use with SimpleRPG"""
from discord.ext import commands

from ..exceptions import HasNoCharacterException


def has_character():
    def predicate(ctx):
        if ctx.message.author.id in ctx.bot.characters:
            return True
        else:
            raise HasNoCharacterException
    return commands.check(predicate)
