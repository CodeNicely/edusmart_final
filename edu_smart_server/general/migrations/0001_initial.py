# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-05 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CUSTOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KEYS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KEYS_LIST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='notice_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='keys',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.KEYS_LIST', to_field='key'),
        ),
        migrations.AddField(
            model_name='custom',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.KEYS_LIST', to_field='key'),
        ),
    ]
