from django.urls import path, re_path
from rest_framework.routers import SimpleRouter
from vehicle import views
from vehicle import data_update

router = SimpleRouter()
router.register('stolen_vehicles', views.StolenCarsViewSet)

urlpatterns = [
    path('stolen_vehicles/<int:pk>', views.DetailsStolenCarsViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    re_path('^vehicle/(?P<make_name>.+)/$', views.ModelsList.as_view()),
]

urlpatterns += router.urls
