from django.contrib import admin
from django.urls import path, include
from taxi.views import *

print("taxi/urls")
urlpatterns = [
    path('', index, name="index"),  # 2
]
