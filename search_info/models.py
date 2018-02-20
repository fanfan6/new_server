from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SearchHistory(models.Model):
    app_id = models.IntegerField(db_index=True)
    report_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    id_card = models.CharField(max_length=64, blank=True, null=True)
    service = models.CharField(max_length=16)
    search_time = models.CharField(max_length=32)
    create_time = models.IntegerField()

    class Meta:
        db_table = 'search_history'
