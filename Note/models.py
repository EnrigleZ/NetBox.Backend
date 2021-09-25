from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True,
                          default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(verbose_name="title", max_length=120, default="")
    content = models.TextField(verbose_name="content")
    image_ids = models.CharField(max_length=1024)
    created_at = models.DateTimeField(verbose_name='createTime', editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updateTime', auto_now=True)
