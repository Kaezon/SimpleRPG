"""
This module contains methods for loading item definitions from YAML files.
"""

from os import listdir
from os.path import isfile, join

from yaml import load, Loader

from ..schematics import ItemSchematic


def load_item_from_file(file_stream):
    """
    Parses an item YAML file.
    args:
        file_stream: A read-mode file stream.
    returns:
        ItemSchematic
    """

    return ItemSchematic(load(file_stream, Loader=Loader))


def load_items(items_path: str):
    """
    Loads item schematics from disk.
    args:
        items_path: Path to item YAML files.
    returns:
        list
    """

    items = []
    for item in listdir(items_path):
        if isfile(join(items_path, item)) \
                and item.lower().endswith('.yml') \
                or item.lower().endswith('.yaml'):
            with open(join(items_path, item)) as yaml_file:
                items.append(load_item_from_file(yaml_file))

    return items
