# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_trip_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='img_url',
            field=models.ImageField(default='media/default.png', upload_to='trip_images'),
        ),
    ]