"""
Django admin stuff
"""
from django.contrib import admin
from base.models import Character, Item, Inventory

class CharacterAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class InventoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character, CharacterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Inventory, InventoryAdmin)
