# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0037_auto_20160819_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='query_id',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='result',
            name='query_id',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
