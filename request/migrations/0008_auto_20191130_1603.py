# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-30 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0007_auto_20191130_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='request_title',
            field=models.CharField(max_length=40),
        ),
    ]