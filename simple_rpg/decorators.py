"""Decorators for use with SimpleRPG"""
from discord.ext import commands


def must_have_character():
    def predicate(ctx):
        # This needs to become a database check
        if ctx.message.author in ctx.bot.characters:
            return True
        ctx.send("You must create a character first!")
        return False
    return commands.check(predicate)
