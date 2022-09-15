from django.urls import path

from taxi.views import index, car, driver

urlpatterns = [
    path("", index, name="index"),
    path("car/", car, name="car"),
    path("driver/", driver, name="driver")
]

app_name = "taxi"
