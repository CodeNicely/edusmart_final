# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_data',
            name='profile_iage',
            field=models.ImageField(default='media/profile/people.png', upload_to='media/profile'),
        ),
    ]
