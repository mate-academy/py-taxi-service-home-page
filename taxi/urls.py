from django.urls import path, include

from taxi.views import index, manufacturers_view, cars_view, drivers_view

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", manufacturers_view, name="manufacturers"),
    path("cars/", cars_view, name="cars"),
    path("drivers/", drivers_view, name="drivers"),
]

app_name = "taxi"
