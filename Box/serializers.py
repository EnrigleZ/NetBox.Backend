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
        if hasattr(instance, 'file_content'):
            try:
                representation['size'] = instance.file_content.size
                representation['path'] = instance.file_content.path
            except FileNotFoundError:
                representation['size'] = 0

        return representation

    # def get_fields(self, *args, **kwargs):
    #     fields = super().get_fields(*args, **kwargs)
    #     request = self.context.get('request')
    #     print(self.context)
    #     # if request is not None and request.method != ''
    #     return fields