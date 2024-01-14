from django.contrib import admin
from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("taxi/", views.index, name="index"),
]
