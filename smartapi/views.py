from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from smartapi.models import Citie
from smartapi.serializers import CitieSerializer


class CitieViewSet(viewsets.ModelViewSet):
    queryset = Citie.objects.all().order_by('id')
    serializer_class = CitieSerializer