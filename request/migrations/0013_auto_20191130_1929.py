# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-30 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0012_auto_20191130_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmodel',
            name='status',
            field=models.CharField(blank=True, choices=[('requested', 'requested'), ('accepted', 'accepted'), ('pending', 'pending'), ('rejected', 'rejected'), ('delivered', 'delivered')], default='requested', max_length=9, null=True),
        ),
    ]
