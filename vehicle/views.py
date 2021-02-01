from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import AdminRenderer
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
import requests

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet
from vehicle.models import StolenVehicle, VehicleMakes, MakeModels

from vehicle.serializers import StolenVehicleSerializer, MakeModelsSerializer
import json


class StolenCarsViewSet(ModelViewSet):
    queryset = StolenVehicle.objects.all()
    serializer_class = StolenVehicleSerializer
    renderer_classes = [AdminRenderer, XMLRenderer, XLSXRenderer]
    filename = 'my_export.xlsx'

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['full_name', 'license_plate', 'vin']
    filterset_fields = ['make_name', 'model', 'year']
    ordering_fields = ['full_name', 'license_plate', 'car_color', 'vin', 'make_name', 'model', 'year']

    def create(self, request, *args, **kwargs):
        data = self.get_make_name(dict(request.data))
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        data.update(serializer.validated_data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_make_name(self, data):
        for k, v in data.items():
            data[k] = v[0]
        url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/' + data['vin'] + '?format=json&modelyear='
        res = requests.get(url)
        result = json.loads(res.text).get("Results")
        result = result[0]
        data["make_name"], data["model"], data["year"] = result.get("Make"),\
                                                         result.get("Model"),\
                                                         result.get("ModelYear")
        return data


class DetailsStolenCarsViewSet(ModelViewSet):
    queryset = StolenVehicle.objects.all()
    serializer_class = StolenVehicleSerializer


class ModelsList(generics.ListAPIView):
    serializer_class = MakeModelsSerializer

    def get_queryset(self):
        make_name = self.kwargs['make_name'].upper()
        make = VehicleMakes.objects.get(makes=make_name)
        return MakeModels.objects.filter(make_id=make.id)
