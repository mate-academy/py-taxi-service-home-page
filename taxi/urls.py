from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("home/", views.index, name="index"),
]
