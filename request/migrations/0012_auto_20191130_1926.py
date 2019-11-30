# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-30 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_auto_20191130_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='status',
        ),
        migrations.AddField(
            model_name='requestmodel',
            name='status',
            field=models.CharField(blank=True, choices=[('accepted', 'accepted'), ('pending', 'pending'), ('rejected', 'rejected'), ('delivered', 'delivered')], default='pending', max_length=9, null=True),
        ),
    ]
