# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0002_unless'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dice', models.IntegerField()),
                ('damage_dice', models.IntegerField()),
                ('damage_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MonsterOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=255)),
                ('number_attacks', models.IntegerField()),
                ('attacks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combat_id', to='mon_app.Combat')),
            ],
        ),
    ]
