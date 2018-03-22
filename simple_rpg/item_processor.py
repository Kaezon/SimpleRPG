"""
The ItemProcessor is a class for processing the effects of item schematics
in a given context.
"""
from .exceptions import NoTargetSpecifiedException


class ItemProcessor(object):
    """Class which processes item schematics in their relevant contexts."""

    def __init__(self, bot):
        self.bot = bot

    def process_item(self, character, item, target=None):
        """
        This method processes an item schematic.
        args:
            character: The character which is using the item.
            item: An item schematic.
        """
        # Make sure a target is specified somewhere
        if target is None:
            if item.target is None:
                raise NoTargetSpecifiedException
            target = item.target

        # Set or validate target
        if target == 'self':
            target = character
        # TODO: more target types

        # Perform the item's actions
        for verb in item.actions:
            if verb.action == 'add_health':
                target.model.health += int(verb.value)
