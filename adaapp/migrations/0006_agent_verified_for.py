# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaapp', '0005_auto_20160914_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='verified_for',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Verificado Por'),
        ),
    ]