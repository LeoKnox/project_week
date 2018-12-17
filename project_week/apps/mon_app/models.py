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