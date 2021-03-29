import logging
from decimal import Decimal
from operator import itemgetter

from django.db import transaction

from smartapi.models.models import City, LinkCity


class CitiesService:

    @classmethod
    def get_cities(cls):
        cities = City.objects.all()
        return cities

    @classmethod
    def get_city(cls, id):
        city = City.objects.prefetch_related('links').get(pk=id)
        return city

    @classmethod
    @transaction.atomic
    def save_cities(cls, data):
        ids = list(map(itemgetter('id'), data['links']))
        ids = [x for i,x in enumerate(ids) if i == 0]


        if data['id'] > 0:
            city = City.objects.prefetch_related('links').get(pk=data['id'])
            links = city.links.exclude(id__in=ids)
            for aux in links:
                aux.delete()
        else:
            city = City()

        city.name = data['name']
        city.latitude = Decimal(data['latitude'])
        city.longitude = Decimal(data['longitude'])
        city.left = Decimal(data['left'])
        city.down = Decimal(data['down'])
        city.right = Decimal(data['right'])
        city.up = Decimal(data['up'])
        city.save()
        for link in data['links']:

            if link['id'] > 0:
                linkdata = LinkCity.objects.get(pk=link['id'])
            else:
                linkdata = LinkCity()

            linkdata.place = link['place']
            linkdata.value = link['value']
            linkdata.city = city
            linkdata.save()

        return City






    


