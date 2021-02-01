import requests
import json
from vehicle.models import VehicleMakes, MakeModels


def update_makes_table(request):
    res_makes = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
    data_makes = json.loads(res_makes.text).get("Results")
    for make in data_makes:
        try:
            check = VehicleMakes.objects.get(id_make=make["Make_ID"])
        except VehicleMakes.DoesNotExist:
            obj_make = VehicleMakes(id_make=make["Make_ID"], makes=make["Make_Name"])
            obj_make.save()

            path = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeid/' + str(make["Make_ID"]) + '?format=json'
            res_models = requests.get(path)
            data_models = json.loads(res_models.text).get("Results")
            for model in data_models:
                model = model.get("Model_Name")
                obj_model = MakeModels(model_name=model, make_id=obj_make)
                obj_model.save()



    # vins = ['3FA6P0VP1HR282209', '5NPE24AFXFH183476', '1FMCU9J94FUA44289', '3VWDP7AJ7DM356782', '5XYKT3A12CG000000']

