# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(db_index=True)),
                ('report_id', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('id_card', models.CharField(blank=True, max_length=64, null=True)),
                ('service', models.CharField(max_length=16)),
                ('search_time', models.CharField(max_length=32)),
                ('create_time', models.IntegerField()),
            ],
            options={
                'db_table': 'search_history',
            },
        ),
    ]
