"""Data manipulation classes for COGs"""

from discord.ext import commands


class MemberConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        if argument == 'everyone' or argument == '@everyone':
            return 'everyone'
        return await super().convert(ctx, argument)


class NumberConverter(commands.Converter):
    async def convert(self, ctx, argument):
        argument = argument.replace(",", "")
        if not argument.isdigit():
            raise commands.BadArgument("That is not a number!")
        if len(argument) > 10:
            raise commands.BadArgument(
                "That number is much too big! Must be less than 999,999,999")
        return int(argument)
