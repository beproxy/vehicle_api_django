from rest_framework import serializers
from vehicle.models import VehicleMakes, StolenVehicle


class VehicleMakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMakes
        fields = '__all__'


class StolenVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StolenVehicle
        fields = '__all__'