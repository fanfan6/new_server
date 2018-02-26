# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0002_auto_20180220_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFeature',
            fields=[
                ('model_feature_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=128)),
                ('created_time', models.BigIntegerField()),
            ],
            options={
                'db_table': 'model_feature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelFeatureRecord',
            fields=[
                ('model_feature_record_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model_running_record_id', models.BigIntegerField()),
                ('model_feature_id', models.IntegerField()),
                ('created_time', models.BigIntegerField()),
            ],
            options={
                'db_table': 'model_feature_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelFeatureVectorRecord',
            fields=[
                ('model_feature_vector_record_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('model_running_record_id', models.BigIntegerField()),
                ('module', models.CharField(max_length=32)),
                ('feature_vector', models.TextField(blank=True, null=True)),
                ('created_time', models.BigIntegerField()),
            ],
            options={
                'db_table': 'model_feature_vector_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ModelRunningRecord',
            fields=[
                ('model_running_record_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=32, null=True)),
                ('user_type', models.IntegerField()),
                ('module', models.CharField(max_length=30)),
                ('category', models.IntegerField()),
                ('score', models.FloatField()),
                ('source', models.CharField(max_length=16)),
                ('created_time', models.BigIntegerField()),
            ],
            options={
                'db_table': 'model_running_record',
                'managed': False,
            },
        ),
    ]
