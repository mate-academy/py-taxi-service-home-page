from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index),
    path("hello/", index, name="index"),
]

app_name = "taxi"
