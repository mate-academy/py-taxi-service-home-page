from django.shortcuts import render

from django.contrib import admin
from django.urls import path
from django.urls import include

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "catalog"
