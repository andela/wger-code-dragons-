# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-16 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_userprofile_api_creation_righ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='api_creation_righ',
        ),
    ]
