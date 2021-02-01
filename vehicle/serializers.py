from rest_framework import serializers
from vehicle.models import VehicleMakes, StolenVehicle, MakeModels


class VehicleMakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMakes
        fields = '__all__'


class MakeModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeModels
        fields = ['model_name',]


class StolenVehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StolenVehicle
        fields = '__all__'
