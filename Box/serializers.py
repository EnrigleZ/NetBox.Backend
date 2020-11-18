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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            size = instance.file_content.size
            representation['size'] = size
        except FileNotFoundError:
            representation['size'] = 0

        print(representation)
        return representation