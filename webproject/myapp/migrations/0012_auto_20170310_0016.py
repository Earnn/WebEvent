# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-09 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170310_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='username',
        ),
    ]
