from django.db import models
import uuid
import os

IMAGE_DIR = 'image_host'

def on_upload(instance, filename):
    id = instance.id
    return os.path.join(IMAGE_DIR, f'{id}.png')

class ImageFile(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True,
                          default=uuid.uuid4, editable=False, unique=True)
    file_content = models.FileField(verbose_name="content", upload_to=on_upload)
    created_at = models.DateTimeField(verbose_name='createTime', editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updateTime', auto_now=True)
