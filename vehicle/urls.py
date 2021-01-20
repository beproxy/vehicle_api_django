from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from vehicle import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vehicles/', views.stolen_vehicle_list),
    path('vehicles/<int:pk>', views.stolen_vehicle_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)