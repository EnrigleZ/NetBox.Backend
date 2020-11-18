from django.db import models
import uuid

class BoxFile(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True,
                          default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name="name", max_length=120)
    description = models.CharField(verbose_name="description", max_length=250)
    file_content = models.FileField(verbose_name="content", upload_to='box_files')
    created_at = models.DateTimeField(verbose_name='createTime', editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updateTime', auto_now=True)
    author = models.CharField(verbose_name='author', max_length=50)
