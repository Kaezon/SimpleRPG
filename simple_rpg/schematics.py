"""
Module containing Item schematics.
Items should be defined in YAML files with this format:
```
health_potion:
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
    action = StringType()
    value = StringType()


class ItemSchematic(Model):
    display_name = StringType()
    item_type = StringType()
    value = IntType()
    target = StringType()
    actions = ListType(ModelType(ActionSchematic))
