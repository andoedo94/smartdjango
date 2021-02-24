from rest_framework import serializers

from smartapi.Models.enums import LinkPlace
from smartapi.Models.models import Citie


class CitieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Citie
        fields = ('id', 'name', 'latitude', 'longitude', 'left', 'down', 'right', 'up', 'created_at', 'updated_at', 'url', 'link')


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


