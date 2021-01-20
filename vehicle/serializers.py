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


class StolenVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StolenVehicle
        fields = '__all__'
        # fields = ['full_name', 'license_plate', 'car_color', 'vin']
        # fields = ['full_name', 'license_plate', 'car_color', 'vin', 'make_name', 'model', 'year']


class DataExtractVinSerializer(serializers.Serializer):
    csrfmiddlewaretoken = serializers.CharField(max_length=100)
    full_name = serializers.CharField(max_length=100)
    license_plate = serializers.CharField(max_length=10)
    car_color = serializers.CharField(max_length=10)
    vin = serializers.CharField(max_length=17)
    make_name = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField(default=0)