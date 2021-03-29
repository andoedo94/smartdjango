from rest_framework import serializers

from smartapi.models.enums import LinkPlace
from smartapi.models.models import City


class CitieSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, max_value=None, min_value=None)
    place = serializers.ChoiceField(LinkPlace.choices)
    value = serializers.CharField(max_length=150)


class CitieSerializerCreate(serializers.Serializer):
    id = serializers.IntegerField(required=False, max_value=None, min_value=None)
    name = serializers.CharField(max_length=150)
    latitude = serializers.DecimalField(max_digits=30, decimal_places=20)
    longitude = serializers.DecimalField(max_digits=30, decimal_places=20)
    left = serializers.DecimalField(max_digits=30, decimal_places=20)
    down = serializers.DecimalField(max_digits=30, decimal_places=20)
    right = serializers.DecimalField(max_digits=30, decimal_places=20)
    up = serializers.DecimalField(max_digits=30, decimal_places=20)
    links = LinkSerializer(required=False, many=True)


