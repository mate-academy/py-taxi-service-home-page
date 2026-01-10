from django.urls import path

from taxi.views import index, drivers, manufacturers, cars

urlpatterns = [
    path("", index, name="index"),
    path("taxi/drivers", drivers, name="drivers"),
    path("taxi/cars", cars, name="cars"),
    path("taxi/manufacturers", manufacturers, name="manufacturers"),
]

app_name = "taxi"
