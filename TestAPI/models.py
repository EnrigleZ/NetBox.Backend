from django.db import models
from django.utils import timezone

import uuid

class TestStruct(models.Model):
  title = models.CharField(verbose_name='title', max_length=50)
  content = models.CharField(verbose_name='content', max_length=200)
  created_at = models.DateTimeField(verbose_name='createTime', editable=False)
  updated_at = models.DateTimeField(verbose_name='updateTime')
  id = models.UUIDField(verbose_name='id', primary_key=True, default=uuid.uuid4, editable=False, unique=True)

  def save(self, *args, **kwargs):
    timestamp = timezone.now()
    if not self.created_at:
      self.created_at = timestamp
    self.updated_at = timestamp
    return super().save(*args, **kwargs)
    
