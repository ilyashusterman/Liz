# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='img_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
