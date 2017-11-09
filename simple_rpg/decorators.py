"""Decorators for use with SimpleRPG"""


def must_have_character(ctx):
    # This needs to become a database check
    if ctx.message.author in ctx.bot.characters:
        return True
    ctx.send("You must create a character first!")
    return False
