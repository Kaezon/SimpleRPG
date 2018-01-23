"""
The ItemProcessor is a class for processing the effects of item schematics
in a given context.
"""


class ItemProcessor(Object):
    """Class which processes item schematics in their relevant contexts."""

    def __init__(self, bot):
        self.bot = bot

    def process_item(self, character, item):
        """
        This method processes an item schematic.
        args:
            character: The character which is using the item.
            item: An item schematic.
        """
        pass
