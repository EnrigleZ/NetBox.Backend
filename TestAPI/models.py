from django.db import models

class TestStruct(models.Model):
  title = models.CharField(verbose_name='title', max_length=50)
  content = models.CharField(verbose_name='content', max_length=200)
