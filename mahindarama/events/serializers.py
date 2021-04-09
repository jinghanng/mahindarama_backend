from rest_framework import serializers
from .models import Event


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class EventSerializer(serializers.ModelSerializer):
    location = StringSerializer(many=True)
    categories = StringSerializer(many=True)
    sangha_name = StringSerializer(many=True)
    publish_by = StringSerializer(many=False)

    class Meta:
        model = Event
        fields = ('__all__')
