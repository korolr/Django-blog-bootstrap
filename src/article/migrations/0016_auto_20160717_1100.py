# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20160717_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords',
            name='name',
            field=models.TextField(max_length=50, unique=True, verbose_name='Search'),
        ),
    ]
