from django.urls import path
from . import views

app_name = "taxi"  # Це namespace

urlpatterns = [
    path("", views.index, name="index"),  # Домашня сторінка
]
