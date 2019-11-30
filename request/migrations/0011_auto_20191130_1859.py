# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-30 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0010_auto_20191130_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='final_product',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='quote',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(blank=True, choices=[('accepted', 'accepted'), ('pending', 'pending'), ('rejected', 'rejected'), ('delivered', 'delivered')], default='pending', max_length=9, null=True),
        ),
    ]