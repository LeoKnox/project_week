from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WeaponManager(models.Manager):
    def weapon_validator(self, postData):
        errors = {}
        if len(postData['weapon']) < 3:
            errors["weapon"] = "Name must be longer than 2 letters."
        return errors

class SpellManager(models.Manager):    
    def spell_validator(self, postData):
        errors = {}
        if len(postData['spell']) < 3:
            errors["spell"] = "Spell name must be longer than 2 letters."
        return errors

class Weapon(models.Model):
    weapon=models.CharField(max_length=255)
    number=models.IntegerField()
    dice=models.IntegerField()
    equip=models.CharField(max_length=255)
    objects = WeaponManager()

class Spell(models.Model):
    spell=models.CharField(max_length=255)
    spell_num=models.IntegerField()
    spell_dice=models.IntegerField()
    spell_type=models.CharField(max_length=255)
    objects = SpellManager()