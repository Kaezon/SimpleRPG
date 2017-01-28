"""
Graphene Nodes
"""
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from base.models import Character, Item, Inventory

class CharacterNode(DjangoObjectType):
    """
    User Node
    """
    class Meta:
        model = Character
        filter_fields = ['name', 'owner']
        interfaces = (relay.Node, )

class ItemNode(DjangoObjectType):
    """
    Item Node
    """
    class Meta:
        model = Item
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class InventoryNode(DjangoObjectType):
    """
    Inventory Node
    """
    model = Inventory
    filter_fields = ['character']
    interfaces = (relay.Node, )

class Query(AbstractType):
    character = relay.Node.Field(CharacterNode)
    all_characters = DjangoFilterConnectionField(CharacterNode)

    item = relay.Node.Field(ItemNode)
    all_items = DjangoFilterConnectionField(ItemNode)

    inventory = relay.Node.Field(InventoryNode)
