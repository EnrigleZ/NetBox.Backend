from TestAPI.models import TestStruct
from rest_framework import serializers

class TimestampField(serializers.Field):
  def to_representation(self, value):
    return round(value.timestamp() * 1000)

class TestStructSerializer(serializers.ModelSerializer):
  id = serializers.UUIDField(read_only=True)
  title = serializers.CharField(required=True)
  content = serializers.CharField(required=False)
  created_at = TimestampField(read_only=True)
  updated_at = TimestampField(read_only=True)

  class Meta:
    model = TestStruct
    fields = '__all__'
