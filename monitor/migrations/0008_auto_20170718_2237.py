# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 05:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_auto_20170718_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='mtp',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 19, 5, 37, 1, 602506, tzinfo=utc)),
        ),
    ]
