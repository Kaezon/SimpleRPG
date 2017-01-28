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
    hp = models.IntegerField()
    ap = models.IntegerField()
    xp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    agility = models.IntegerField()
    luck = models.IntegerField()

class Item(models.Model):
    """
    Represents an item
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)

class Inventory(models.Model):
    """
    The relationship between Items and Characters
    """
    character = models.ForeignKey(Character)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
