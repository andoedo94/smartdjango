
from http import HTTPStatus
import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from smartapi.jobs.downloadfigures import download_figures
from smartapi.models.services.citiesServices import CitiesService
from smartapi.serializers import CitieSerializer, CitieSerializerCreate


class CitieViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], name='Get cities')
    def getcities(self, request):
        try:
            cities = CitiesService.get_cities()
            citiesserialized = CitieSerializer(cities, many=True)
            return Response({'success': True, 'data': citiesserialized.data}, HTTPStatus.OK)
        except Exception as exception:
            logging.error("Error in server detail: " + str(exception))
            return Response({'success': False}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], name='Get city', url_path=r'getcity/(?P<id>\d+)')
    def getcity(self, request, id):
        try:
            city = CitiesService.get_city(id)
            citiesserialized = CitieSerializerCreate(city)
            return Response({'success': True, 'data': [citiesserialized.data]}, HTTPStatus.OK)
        except Exception as exception:
            logging.error("Error in server detail: " + str(exception))
            return Response({'success': False}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], name='Create city')
    def save(self, request):
        try:
            serializer = CitieSerializerCreate(data=request.data)
            if serializer.is_valid():
                cities = CitiesService.save_cities(serializer.validated_data)
                return Response({'success': True}, HTTPStatus.CREATED)
            else:
                return Response({'success': False, 'errors': serializer.errors},
                                status=HTTPStatus.UNPROCESSABLE_ENTITY)
        except Exception as exception:
            logging.error(" Error in server detail: " + str(exception))
            return Response({'success': False}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def test(self, request):

        test = download_figures(7, 2, 0)
        return Response({'success': True, 'test': str(test)})



