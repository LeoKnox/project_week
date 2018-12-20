from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Useless(models.Model):
    one=models.CharField(max_length=255)
    two=models.CharField(max_length=255)
    three=models.CharField(max_length=255)

class Unless(models.Model):
    x=models.CharField(max_length=255)
    y=models.CharField(max_length=255)
    z=models.ForeignKey(Useless, related_name="useless_id")

class Combat(models.Model):
    name=models.CharField(max_length=255)
    dice=models.IntegerField()
    damage_dice=models.IntegerField()
    damage_type=models.CharField(max_length=255)

class MonsterOne(models.Model):
    name=models.CharField(max_length=255)
    style=models.CharField(max_length=255)
    attacks=models.ForeignKey(Combat, related_name="combat_id")
    number_attacks=models.IntegerField()
    