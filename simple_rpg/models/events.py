"""
Module containing models of verious events characters can
participate in.
"""
from discord import Client

from ..constants import CHARACTER_CREATION_STAGE


class Event:
    def __init__(self, characters: list, client: Client):
        self.characters = characters
        self.client = client


class CharacterCreation(event):
    """The character creation process"""
    def __init__(self, character: Character, client: Client):
        super().__init__(characters, client)
        self.stage = CHARACTER_CREATION_STAGE.START


class NPCBattle(event):
    """A battle between an npc and one or more characters"""
    def __init__(self, characters: list, client: Client):
        super().__init__(characters, client)


class GamblingSession(event):
    """A gambling session with one or more characters"""
    def __init__(self, characters: list, client: Client):
        super().__init__(characters, client)
