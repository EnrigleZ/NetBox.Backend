from Box.models import BoxFile
from rest_framework import serializers

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return round(value.timestamp() * 1000)

class BoxFileSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False)
    created_at = TimestampField(read_only=True)
    updated_at = TimestampField(read_only=True)
    class Meta:
        model = BoxFile
        fields = '__all__'
