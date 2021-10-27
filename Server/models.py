from django.db import models
from rest_framework import serializers

# Create your models here.
class GitCommit(models.Model):
    id = models.CharField(primary_key=True, editable=False, unique=True, max_length=40)
    message = models.CharField(max_length=1024)
    url = models.CharField(max_length=256)
    committer = models.CharField(max_length=64)
    timestamp = models.IntegerField()
    ref = models.CharField(max_length=256, default='')
    qa_checked = models.CharField(max_length=64, default='')

class GitCommitSerializer(serializers.Serializer):
    id = serializers.CharField()
    message = serializers.CharField()
    url = serializers.CharField()
    committer = serializers.CharField()
    timestamp = serializers.IntegerField()
    ref = serializers.CharField()
    qa_checked = serializers.CharField()

    class Meta:
        model = GitCommit
