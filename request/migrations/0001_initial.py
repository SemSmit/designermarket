# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-28 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_title', models.CharField(blank=True, max_length=40, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('request', models.TextField(blank=True, null=True)),
                ('graphic_type', models.CharField(blank=True, choices=[('Poster', 'poster'), ('Icon', 'icon'), ('Logo', 'logo'), ('Different', 'different')], max_length=9, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('date_requested', models.DateTimeField(blank=True, null=True)),
                ('wireframe', models.ImageField(blank=True, upload_to='')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
    ]
