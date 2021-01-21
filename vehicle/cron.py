import datetime
import logging

from vehicle.models import VehicleMakes, MakeModels
import requests
import json


# Я б конечно лучше вытаскивал последнюю дату обновления таблицы и потом отнее отсчитывал когда апдейтить
# но в SQLite этой возможости так и не нашел( это есть в MySQL и PostgreSQL
def scheduled_task():
    dt = str(datetime.now())
    logging.basicConfig(filename='cron_log.log', level=logging.INFO)
    logging.info('----- Starting process at ' + dt)

    try:
        VehicleMakes.objects.all().delete()
        MakeModels.objects.all().delete()
        logging.info('deleted tables: VehicleMakes, MakeModels')
    except Exception as e:
        print(e)
    res_makes = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json')
    data_makes = json.loads(res_makes.text).get("Results")
    for make in data_makes:
        try:
            VehicleMakes.objects.get(id_make=make["Make_ID"])
        except VehicleMakes.DoesNotExist:
            obj_make = VehicleMakes(id_make=make["Make_ID"], makes=make["Make_Name"])
            obj_make.save()

            path = 'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeid/' + str(
                make["Make_ID"]) + '?format=json'
            res_models = requests.get(path)
            data_models = json.loads(res_models.text).get("Results")
            for model in data_models:
                model = model.get("Model_Name")
                obj_model = MakeModels(model_name=model, make_id=obj_make)
                obj_model.save()
    logging.info('created tables: VehicleMakes, MakeModels')
    logging.info('----- End of process at ' + dt)
