# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BestRoute', '0005_crimedatapoint_occurred_on_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crimedatapoint',
            old_name='offense_codd',
            new_name='offense_code',
        ),
    ]
