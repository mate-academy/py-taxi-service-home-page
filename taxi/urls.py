from django.contrib import admin
from django.urls import path
from taxi.views import homeland
from taxi.views import index



urlpatterns = [
    path("homeland/", homeland),
    path("", index)
]