"""Custom exceptions for the SimpleRPG bot"""
from discord.ext.commands import CommandError


class HasNoCharacterException(CommandError):
    """
    Exception raised when the context author does not have a corresponding
    character.
    """
    pass


class MatchedMultipleMembersException(CommandError):
    """
    Raised when an argument matched multiple memebrs, but should have only
    matched one.
    """
    pass


class MemberNotFoundException(CommandError):
    """Raised when an attempt to resolve one or more members fails."""
    pass


class NoTargetSpecifiedException(CommandError):
    """
    Raised when an action requiring a taget is invoked, but no target is
    specified.
    """
    pass
