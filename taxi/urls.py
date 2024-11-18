from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),
    path("manufacturers/", views.manufacturer_list, name="manufacturer_list"),
    path("cars/", views.car_list, name="car_list"),
    path("drivers/", views.driver_list, name="driver_list"),
]
