from django.urls import path
from . import views

app_name = "taxi"  # ключове слово

urlpatterns = [
    path("", views.index, name="index"),  # домашня сторінка
]
