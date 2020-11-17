from Box.models import BoxFile
from rest_framework import serializers


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return round(value.timestamp() * 1000)

class BoxFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxFile
        exclude = ('file_content', )