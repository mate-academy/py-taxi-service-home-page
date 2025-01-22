from django.urls import path
from taxi.views import index, manufacturers, cars, drivers

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", manufacturers, name="manufacturers"),
    path("cars/", cars, name="cars"),
    path("drivers/", drivers, name="drivers"),
]
