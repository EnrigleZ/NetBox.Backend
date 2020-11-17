from TestAPI.models import TestStruct
from rest_framework import serializers

class TestStructSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = TestStruct
    fields = ['title', 'content', 'created_at', 'updated_at']
