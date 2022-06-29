from django.urls import path

from taxi.views import index, drivers

urlpatterns = [
    path("", index, name="index"),
    path("drivers/", drivers, name="drivers")
]

app_name = "taxi"
