# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_trip_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
