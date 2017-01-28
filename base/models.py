"""
Models for the base game
"""
from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    """
    Represents a game character
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    hp = models.Integer()
    ap = models.Integer()
    xp = models.Integer()
    attack = models.Integer()
    defense = models.Integer()
    agility = models.Integer()
    luck = models.Integer()

class Item(models.Model):
    """
    Represents an item
    """
    name = models.CharField(max_length=50)
    description = models.Charfield(256)

class Inventory(models.Model):
    """
    The relationship between Items and Characters
    """
    character = models.ForeignKey(Character)
    item = models.ForeignKey(Item)
    quantity = models.Integer()
