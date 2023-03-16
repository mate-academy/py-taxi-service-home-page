from django.urls import path
from django.contrib import admin

from taxi.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "taxi"
