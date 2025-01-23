from . import views
from django.urls import path

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),
]
