"""
Module containing models of verious events characters can
participate in.
"""


class event:
    def __init__(self, characters: list):
        self.characters = characters


class npc_battle(event):
    """A battle between an npc and one or more characters"""
    def __init__(self, characters: list):
        super(characters)


class gambling_session(event):
    """A gambling session with one or more characters"""
    def __init__(self, characters: list):
        super(characters)
