# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfoForStatistics(models.Model):
    app_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=64, verbose_name='姓名')
    id_card = models.CharField(max_length=64, verbose_name='身份证号')
    phone = models.CharField(max_length=64, verbose_name='手机号')
    sex = models.CharField(max_length=8, verbose_name='性别')
    source = models.CharField(max_length=64, default='', validators='资产包标签')
    education = models.CharField(max_length=256, null=True, verbose_name='教育程度')
    jobs = models.CharField(max_length=256, null=True, verbose_name='职业')
    live_long = models.CharField(max_length=128, null=True, validators='居住地经度')
    live_lat = models.CharField(max_length=128, null=True, validators='居住地维度')
    application_long = models.CharField(max_length=128, null=True, validators='申请地经度')
    application_lat = models.CharField(max_length=128, null=True, validators='申请地维度')
    application_time = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        db_table = 'user_info'


class ModelFeatureRecord(models.Model):
    model_feature_record_id = models.BigAutoField(primary_key=True)
    model_running_record_id = models.BigIntegerField()
    model_feature_id = models.IntegerField()
    created_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_feature_record'


class ModelFeatureVectorRecord(models.Model):
    model_feature_vector_record_id = models.BigAutoField(primary_key=True)
    model_running_record_id = models.BigIntegerField()
    module = models.CharField(max_length=32)
    feature_vector = models.TextField(blank=True, null=True)
    created_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_feature_vector_record'


class ModelRunningRecord(models.Model):
    model_running_record_id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_type = models.IntegerField()
    module = models.CharField(max_length=30)
    category = models.IntegerField()
    score = models.FloatField()
    source = models.CharField(max_length=16)
    created_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_running_record'


class ModelFeature(models.Model):
    model_feature_id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=128)
    created_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_feature'
