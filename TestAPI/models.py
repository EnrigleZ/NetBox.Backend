from django.db import models
from django.utils import timezone

import uuid

class TestStruct(models.Model):
  title = models.CharField(verbose_name='title', max_length=50)
  content = models.CharField(verbose_name='content', max_length=200)
  created_at = models.DateTimeField(verbose_name='createTime', editable=False, auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updateTime', auto_now=True)
  id = models.UUIDField(verbose_name='id', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
