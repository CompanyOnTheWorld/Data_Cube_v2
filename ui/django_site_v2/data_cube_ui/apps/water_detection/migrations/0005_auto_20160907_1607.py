# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_detection', '0004_auto_20160906_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resulttype',
            old_name='product_type',
            new_name='result_type',
        ),
    ]
