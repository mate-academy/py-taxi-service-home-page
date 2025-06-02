from django.urls import path
from . import views

app_name = "taxi"  # ← обов'язково

urlpatterns = [
    path("", views.index, name="index"),
]
