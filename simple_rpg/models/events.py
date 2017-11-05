"""
Module containing models of verious events characters can
participate in.
"""
from discord import Client


class event:
    def __init__(self, characters: list, client: Client):
        self.characters = characters
        self.client = client


class character_creation(event):
    """The character creation process"""
    def __init__(self, characters: list, client: Client):
        super(characters, client)


class npc_battle(event):
    """A battle between an npc and one or more characters"""
    def __init__(self, characters: list, client: Client):
        super(characters, client)


class gambling_session(event):
    """A gambling session with one or more characters"""
    def __init__(self, characters: list, client: Client):
        super(characters, client)
