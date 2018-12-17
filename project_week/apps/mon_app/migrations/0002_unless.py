# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-17 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mon_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unless',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=255)),
                ('y', models.CharField(max_length=255)),
                ('z', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useless_id', to='mon_app.Useless')),
            ],
        ),
    ]