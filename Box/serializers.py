from Box.models import BoxFile
from rest_framework import serializers

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return round(value.timestamp() * 1000)

class BoxFileSerializer(serializers.ModelSerializer):
    author = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    created_at = TimestampField(read_only=True)
    updated_at = TimestampField(read_only=True)
    file_content = serializers.FileField(required=False)
    # box_file_area = serializers.CharField(source='box_file_area', default=None)

    class Meta:
        model = BoxFile
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

    def create(self, validated_data):
        print(validated_data)
        return BoxFile.objects.create(**validated_data)

# class BoxFileContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         mode = BoxFile
#         fields = ('id', 'file_content')
