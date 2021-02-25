# Create your views here.
from http import HTTPStatus
import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from smartapi.models.services import CitiesService
from smartapi.serializers import CitieSerializer, CitieSerializerCreate


class CitieViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def getcities(self, request):
        try:
            cities = CitiesService.get_cities()
            citiesserialized = CitieSerializer(cities, many = True)
            return Response({'success': True, 'data': citiesserialized.data}, HTTPStatus.OK)
        except Exception as exception:
            logging.error("Error in server detail: " + str(exception))
            return Response({'success': False}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], name='Create ciudad')
    def save(self, request):
        try:
            serializer = CitieSerializerCreate(data=request.data)
            if serializer.is_valid():
                #ddddddddddddddddddddddddddd
                return Response({'success': True}, HTTPStatus.CREATED)
            else:
                return Response({'success': False, 'errors': serializer.errors},
                                status=HTTPStatus.UNPROCESSABLE_ENTITY)
        except Exception as exception:
            logging.error("Error in server detail: " + str(exception))
            return Response({'success': False}, HTTPStatus.INTERNAL_SERVER_ERROR)



