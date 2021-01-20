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


def create_stolen_data():
    vins = ['3FA6P0VP1HR282209', '5NPE24AFXFH183476', '1FMCU9J94FUA44289', '3VWDP7AJ7DM356782', '5XYKT3A12CG000000']
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeid/'
    format = '?format=json&modelyear='
    year = '2011'
    for i in vins:
        res = requests.get(url + i + format + year)
        data = json.loads(res.text).get("Results")
        make_name = data.get('Make')
        make_id = data.get('MakeID')
        res_1 = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeid/'
                             + {make_id} + '?format=json')
        data_1 = json.loads(res_1.text).get("Results")
        for i in data_1:
            obj = VehicleMakes(id_make=i["Make_ID"], makes=i["Make_Name"])
            obj.save()
