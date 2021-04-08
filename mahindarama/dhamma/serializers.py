from rest_framework import serializers
from .models import Dhamma

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class DhammaSerializer(serializers.ModelSerializer):
    location = StringSerializer(many=True)
    categories = StringSerializer(many=True)
    sangha_name = StringSerializer(many=True)
    media_type = StringSerializer(many=False)
    language = StringSerializer(many=False)

    class Meta:
        model = Dhamma
        fields = ('__all__')
