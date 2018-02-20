# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(db_index=True)),
                ('service', models.CharField(db_index=True, max_length=16)),
                ('clicks', models.CharField(max_length=16)),
                ('date', models.CharField(db_index=True, max_length=32)),
                ('create_time', models.IntegerField()),
            ],
            options={
                'db_table': 'count_click',
            },
        ),
    ]
