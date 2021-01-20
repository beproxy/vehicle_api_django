from django.urls import path, re_path
# from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views
from rest_framework.routers import SimpleRouter
from vehicle import views
from vehicle import data_update

router = SimpleRouter()
router.register('stolen_vehicles', views.StolenCarsViewSet)
# router.register('models', MakeModelsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('stolen_vehicles/<int:pk>', views.DetailsStolenCarsViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('vehicle/<str:makes>', views.ModelsList.as_view()),
    re_path('^vehicle/(?P<make_name>.+)/$', views.ModelsList.as_view()),

    # path('update_makes/', data_update.update_makes_table),
]

urlpatterns += router.urls
