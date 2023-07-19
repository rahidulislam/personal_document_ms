from rest_framework import serializers
from .models import Document
from .utils import get_file_format

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id','title', 'description', 'file', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["format"] = instance.file_format
        return data
    
class DocumentShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('shared_with',)