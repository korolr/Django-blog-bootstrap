# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 16:09
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20160716_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='article.Category'),
        ),
    ]
