from django.urls import path

from taxi.views import index, cars, manufacturers, drivers


app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    path("cars_list", cars, name="cars_list"),
    path("manufacturers_list", manufacturers, name="manufacturers_list"),
    path("drivers_list", drivers, name="drivers_list"),
]
