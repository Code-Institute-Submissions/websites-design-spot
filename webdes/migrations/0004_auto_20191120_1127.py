# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-20 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdes', '0003_auto_20191120_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
