from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
    path("cars/", index, name="cars"),
    path("drivers/", index, name="drivers"),
    path("manufacturers/", index, name="manufacturers"),
]

app_name = "taxi"
