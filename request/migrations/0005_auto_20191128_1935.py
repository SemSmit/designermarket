# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-28 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20191128_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='buyer',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
