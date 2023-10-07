from django.urls import path

from taxi.views import index, cars, drivers, manufacturers

urlpatterns = [
    path("", index, name="index"),
    path("cars/", cars, name="cars"),
    path("drivers/", drivers, name="drivers"),
    path("manufacturers/", manufacturers, name="manufacturers"),
]

app_name = "taxi"
