from django.urls import path

from taxi.views import index, manufacturer, car, driver

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", manufacturer, name="manufacturers"),
    path("cars/", car, name="cars"),
    path("drivers/", driver, name="drivers"),
]

app_name = "taxi"
