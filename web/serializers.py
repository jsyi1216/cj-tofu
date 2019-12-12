from web.models import ImageUpload
from rest_framework import serializers

class PredictSerializer(serializers.ImageField):
    class Meta:
        model = ImageUpload
        fields = '__all__'
