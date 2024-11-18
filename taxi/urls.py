from django.contrib import admin
from django.urls import path, include

from taxi import views

urlpatterns = [
    path("", views.index, name="index"),
]

app_name = "taxi"
