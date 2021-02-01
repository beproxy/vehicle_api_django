from django.db import models

class VehicleMakes(models.Model):
    id_make = models.IntegerField(default=0)
    makes = models.CharField(max_length=50)

class MakeModels(models.Model):
    model_name = models.CharField(max_length=50)
    make_id = models.ForeignKey(VehicleMakes, on_delete=models.CASCADE)


class StolenVehicle(models.Model):
    full_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=10)
    car_color = models.CharField(max_length=10)
    vin = models.CharField(max_length=17)
    make_name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
