from .models import ImageFile
from rest_framework import serializers

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return round(value.timestamp() * 1000)

class ImageFileSerializer(serializers.ModelSerializer):
    created_at = TimestampField(read_only=True)
    updated_at = TimestampField(read_only=True)
    file_content = serializers.FileField(required=False)

    class Meta:
        model = ImageFile
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['exist'] = False
        if hasattr(instance, 'file_content'):
            try:
                representation['size'] = instance.file_content.size
                representation['path'] = instance.file_content.path
                representation['exist'] = True
            except FileNotFoundError:
                representation['size'] = 0
            except:
                pass

        return representation
