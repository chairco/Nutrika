# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrition',
            old_name='unit_calories',
            new_name='calories_unit',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='unit_carbs',
            new_name='carbs_unit',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='unit_fat',
            new_name='fat_unit',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='unit_protein',
            new_name='protein_unit',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='unit_water',
            new_name='water_unit',
        ),
    ]