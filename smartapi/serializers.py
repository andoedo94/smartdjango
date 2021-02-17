from rest_framework import serializers

from .models import Citie

class CitieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citie
        fields = ('name', 'latitude', 'longitude', 'left', 'down', 'right', 'up', 'created_at', 'updated_at', 'url', 'link')