# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-14 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('like_books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='book',
        ),
        migrations.RemoveField(
            model_name='user',
            name='books',
        ),
    ]
