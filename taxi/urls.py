from django.contrib import admin

from django.urls import path, include

from taxi.views import index


app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
]

