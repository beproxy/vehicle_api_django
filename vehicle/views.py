from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from vehicle.models import StolenVehicle

from vehicle.serializers import StolenVehicleSerializer, VehicleMakesSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class StolenCarsViewSet(ModelViewSet):
    serializer_class = StolenVehicleSerializer
    queryset = StolenVehicle.objects.all()


@api_view(['GET', 'POST'])
def stolen_vehicle_list(request):
    if request.method == 'GET':
        stolen_vehicle = StolenVehicle.objects.all()
        serializer = StolenVehicleSerializer(stolen_vehicle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StolenVehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def stolen_vehicle_detail(request, pk):
    try:
        stolen_vehicle = StolenVehicle.objects.get(pk=pk)
    except StolenVehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StolenVehicleSerializer(stolen_vehicle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StolenVehicleSerializer(stolen_vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stolen_vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
