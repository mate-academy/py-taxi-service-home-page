from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", index, name="manufacturers"),
    path("cars/", index, name="cars"),
    path("drivers/", index, name="drivers"),
]

app_name = "taxi"
