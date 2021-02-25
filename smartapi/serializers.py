from rest_framework import serializers

from smartapi.models.enums import LinkPlace
from smartapi.models.models import Citie


class CitieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citie
        fields = '__all__'


class LinkSerializer(serializers.Serializer):
    place = serializers.ChoiceField(LinkPlace.choices)
    value = serializers.CharField(max_length=150)


class CitieSerializerCreate(serializers.Serializer):

    name = serializers.CharField(max_length=150)
    latitude = serializers.DecimalField(max_digits=None, decimal_places=None)
    longitude = serializers.DecimalField(max_digits=None, decimal_places=None)
    left = serializers.DecimalField(max_digits=None, decimal_places=None)
    down = serializers.DecimalField(max_digits=None, decimal_places=None)
    right = serializers.DecimalField(max_digits=None, decimal_places=None)
    up = serializers.DecimalField(max_digits=None, decimal_places=None)
    links = LinkSerializer(required=False, many=True)


