"""
Graphene Nodes
"""
import logging
import graphene
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from django.contrib.auth.models import User
from base.models import Character, Item, Inventory
from .settings import (
    CHARACTER_STARTING_POINTS, CHARACTER_BASE_HEALTH,
    CHARACTER_BASE_ACTION_POINTS)

class UserNode(DjangoObjectType):
    """
    User Node
    """
    class Meta:
        model = User
        filter_fields = ['username', 'email']
        interfaces = (relay.Node, )

class CharacterNode(DjangoObjectType):
    """
    Character Node
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
    class Meta:
        model = Inventory
        filter_fields = ['character']
        interfaces = (relay.Node, )

class CreateCharacter(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        owner_id = graphene.String(required=True)

    ok = graphene.Boolean()
    character = graphene.Field(CharacterNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        owner_id = from_global_id(input.get('owner_id'))[1]
        character = Character(
            name=input.get('name'),
            owner=User.objects.get(pk=owner_id),
            hp=CHARACTER_BASE_HEALTH,
            hp_max=CHARACTER_BASE_HEALTH,
            ap=CHARACTER_BASE_ACTION_POINTS,
            ap_max=CHARACTER_BASE_ACTION_POINTS,
            xp=0,
            level=1,
            attack=0,
            defense=0,
            agility=0,
            luck=0,
            skill_points=CHARACTER_STARTING_POINTS)
        character.save()
        return CreateCharacter(character=character, ok=True)

class BaseMutations(graphene.ObjectType):
    create_character = CreateCharacter.Field()

class Query(AbstractType):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    character = relay.Node.Field(CharacterNode)
    all_characters = DjangoFilterConnectionField(CharacterNode)

    item = relay.Node.Field(ItemNode)
    all_items = DjangoFilterConnectionField(ItemNode)

    inventory = relay.Node.Field(InventoryNode)
