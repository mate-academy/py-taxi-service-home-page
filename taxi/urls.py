from django.urls import path, include
from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index")
]
