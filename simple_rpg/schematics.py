"""
Module containing Item schematics.
Items should be defined in YAML files with this format:
```
identifier: health_potion
display_name: Health Potion
item_type: consumable
value: 10
target: self
actions:
- action: add_health
  value: 25
```
"""

from schematics import Model
from schematics.types import IntType, StringType, ModelType, ListType


class ActionSchematic(Model):
    action = StringType(required=True)
    value = StringType(required=True)


class StatsSchematic(Model):
    strength = IntType(required=True)
    dexterity = IntType(required=True)
    agility = IntType(required=True)
    defense = IntType(required=True)


class ItemSchematic(Model):
    identifier = StringType(required=True)
    display_name = StringType(required=True)
    item_type = StringType(required=True)
    value = IntType(required=True)


class ConsumableSchematic(ItemSchematic):
    target = StringType(required=True)
    actions = ListType(ModelType(ActionSchematic), required=True)


class EquipmentSchematic(ItemSchematic):
    equip_slot = StringType(required=True)
    stat_modifiers = ModelType(StatsSchematic, required=True)
