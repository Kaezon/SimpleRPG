"""Module containing the project's enums."""

from enum import Enum


EQUIPMENT_DICT = dict.fromkeys(
    ['head', 'body', 'left_hand', 'right_hand', 'feet'])


class CHARACTER_CREATION_STAGE(Enum):
    """An Enum of the stages in the character creation process"""
    START = 0
    CLASS = 1
    ALLOCATE_STATS = 2
    SELECT_ABILITIES = 3


class CHARACTER_STATE(Enum):
    """An Enum of character states"""
    IDLE = 0
    UNCONSCIOUS = 1
    FIGHTING = 2
    GAMBLING = 3
