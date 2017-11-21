"""Custom exceptions for the SimpleRPG bot"""
from discord.ext.commands import CommandError


class HasNoCharacterException(CommandError):
    """
    Exception raised when the context author does not have a corresponding
    character.
    """
    pass
