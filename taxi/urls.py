from django.urls import path

from taxi.views import index, car, driver

urlpatterns = [
    path("", index),
    path("car/", car),
    path("driver/", driver)
]

app_name = "taxi"
