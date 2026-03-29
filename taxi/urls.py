from django.urls import path

from taxi.views import index


app_name = "taxi"
urlpatterns = [
    path("", index, name="index"),
    path("drivers/", index, name="driver-list"),
    path("cars/", index, name="car-list"),
    path("manufacturers/", index, name="manufacturer-list"),
]
