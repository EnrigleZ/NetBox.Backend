from django.db import models

# Create your models here.
class GitCommit(models.Model):
    id = models.CharField(primary_key=True, editable=False, unique=True, max_length=40)
    message = models.CharField(max_length=1024)
    url = models.CharField(max_length=256)
    committer = models.CharField(max_length=64)
    timestamp = models.IntegerField()
