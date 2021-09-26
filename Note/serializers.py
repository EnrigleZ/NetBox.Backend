from .models import Note
from rest_framework import serializers

SHORT_CONTENT_MAX_LENGTH = 100

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return round(value.timestamp() * 1000)

class NoteSerializer(serializers.ModelSerializer):
    created_at = TimestampField(read_only=True)
    updated_at = TimestampField(read_only=True)
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    image_ids = serializers.CharField(required=False)

    class Meta:
        model = Note
        fields = '__all__'

    def to_representation(self, instance):
        is_short_content = self.context.get('short', False)
        representation = super().to_representation(instance)
        representation['image_ids'] = representation['image_ids'].split()
        if is_short_content:
            representation['content'] = representation['content'][:SHORT_CONTENT_MAX_LENGTH]

        return representation
