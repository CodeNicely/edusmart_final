# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teachers_data_profile_iage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers_data',
            name='profile_iage',
            field=models.ImageField(default='profile/people.png', upload_to='profile'),
        ),
    ]