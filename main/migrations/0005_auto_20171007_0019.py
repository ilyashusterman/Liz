# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171007_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(default='default.png', upload_to='trip_images'),
        ),
    ]
