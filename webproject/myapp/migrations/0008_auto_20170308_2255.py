# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-08 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20170308_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='pic',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
