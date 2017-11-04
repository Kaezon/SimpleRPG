"""Module containing the project's constants."""

from enum import Enum


EQUIPMENT_DICT = dict.fromkeys(
    ['head', 'body', 'left_hand', 'right_hand', 'feet'])


class CHARACTER_STATE(Enum):
    """An Enum of character states"""
    IDLE = 0
    UNCONSCIOUS = 1
    FIGHTING = 2
    GAMBLING = 3
