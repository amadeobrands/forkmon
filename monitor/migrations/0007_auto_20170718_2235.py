# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 05:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_node_mtp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='mtp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 19, 5, 35, 59, 86546)),
        ),
    ]
