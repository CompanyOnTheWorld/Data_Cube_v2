# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0027_auto_20160720_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='clean_pixel_count',
            field=models.IntegerField(default=0),
        ),
    ]
