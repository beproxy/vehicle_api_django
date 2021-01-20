from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from vehicle.models import StolenVehicle, VehicleMakes, MakeModels

from vehicle.serializers import StolenVehicleSerializer, VehicleMakesSerializer, MakeModelsSerializer,\
    DataExtractVinSerializer

from django.http import JsonResponse
import json



class DataExtractVin:
    def __init__(self, csrfmiddlewaretoken, full_name, license_plate, car_color, vin, make_name, model, year):
        self.csrfmiddlewaretoken = csrfmiddlewaretoken
        self.full_name = full_name
        self.license_plate = license_plate
        self.car_color = car_color
        self.vin = vin
        self.make_name = make_name
        self.model = model
        self.year = year


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class StolenCarsViewSet(ModelViewSet):
    queryset = StolenVehicle.objects.all()
    serializer_class = StolenVehicleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['make_name', 'model', 'year']

    def create(self, request, *args, **kwargs):

        print('request', request.data)
        data = self.get_make_name(dict(request.data))
        # a = dict(request.data)
        print('data', data)
        serializer = self.get_serializer(data=data)
        # print('1', serializer)
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

# class MakeModelsViewSet(ModelViewSet):
#     serializer_class = MakeModelsSerializer
#     queryset = MakeModels.objects.all()
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['full_name', 'license_plate', 'car_color', 'vin', 'make_name', 'model', 'year']
