from rest_framework import serializers
from .models import WineData

class WineDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fixed_acidity = serializers.FloatField()
    volatile_acidity = serializers.FloatField()
    citric_acid = serializers.FloatField()
    residual_sugar = serializers.FloatField()
    chlorides = serializers.FloatField()
    free_sulfur_dioxide = serializers.FloatField()
    total_sulfur_dioxide = serializers.FloatField()
    density = serializers.FloatField()
    pH = serializers.FloatField()
    sulphates = serializers.FloatField()
    alcohol = serializers.FloatField()
    quality = serializers.IntegerField()

    def create(self, validated_data):
        """Tworzenie nowego rekordu"""
        return WineData(**validated_data)

    def update(self, instance, validated_data):
        """Aktualizacja istniejącego rekordu"""
        instance.fixed_acidity = validated_data.get('fixed_acidity', instance.fixed_acidity)
        instance.volatile_acidity = validated_data.get('volatile_acidity', instance.volatile_acidity)
        instance.citric_acid = validated_data.get('citric_acid', instance.citric_acid)
        instance.residual_sugar = validated_data.get('residual_sugar', instance.residual_sugar)
        instance.chlorides = validated_data.get('chlorides', instance.chlorides)
        instance.free_sulfur_dioxide = validated_data.get('free_sulfur_dioxide', instance.free_sulfur_dioxide)
        instance.total_sulfur_dioxide = validated_data.get('total_sulfur_dioxide', instance.total_sulfur_dioxide)
        instance.density = validated_data.get('density', instance.density)
        instance.pH = validated_data.get('pH', instance.pH)
        instance.sulphates = validated_data.get('sulphates', instance.sulphates)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.quality = validated_data.get('quality', instance.quality)

        return instance