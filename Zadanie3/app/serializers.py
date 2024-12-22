from rest_framework import serializers
from .models import Klasa

class KlasaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    x = serializers.FloatField()
    y = serializers.FloatField()

    def create(self, validated_data):
        """Tworzenie nowego rekordu"""
        return Klasa(**validated_data)

    def update(self, instance, validated_data):
        """Aktualizacja istniejącego rekordu"""
        instance.name = validated_data.get('name', instance.name)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        return instance