# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0007_result_data_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='resulttype',
            name='blue',
            field=models.CharField(default='asdf', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resulttype',
            name='green',
            field=models.CharField(default='123', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resulttype',
            name='red',
            field=models.CharField(default='123', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resulttype',
            name='result_id',
            field=models.CharField(default='123', max_length=25),
            preserve_default=False,
        ),
    ]
