"""Module containing the Item class"""


class Item(object):
    """An Item that can be used by characters"""

    def __init__(self, schematic):
        self.schematic = schematic

    def process_schematic(self, owner, target):
        """Process the effects of this item"""
        pass
