from django.db import models
import uuid

class BoxFileArea(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True,
                         default=uuid.uuid4, editable=False, unique=True)
    area_name = models.CharField(verbose_name="areaName", max_length=120)
    password = models.CharField(verbose_name="password", max_length=256)
    need_password = models.BooleanField()

