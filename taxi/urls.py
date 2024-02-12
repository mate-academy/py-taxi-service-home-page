from django.urls import path

from .views import index, cars, manufactures, drivers

urlpatterns = [
    path("", index, name="index"),
    path("cars/", cars, name="cars"),
    path("manufactures/", manufactures, name="manufactures"),
    path("drivers/", drivers, name="drivers"),
]

app_name = "taxi"
