# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20160716_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_article',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
