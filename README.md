# Vehicle api django

### Settings period for auto update of data in tables

CRONJOBS = [
    ('* * * */1 *', 'vehicle.cron.scheduled_task')
]

(* min * hour * day * month * year)

Apply settings: python manage.py crontab add

Change or remove cron timer: python manage.py crontab remove

### Endpoints:

Datas stolen cars

/api/stolen_vehicles/

Details of stolen car

/api/stolen_vehicles/<int:pk>/

Return list of models vehicle

/api/vehicle/<make_name>/

### Run server:

python manage.py runserver
