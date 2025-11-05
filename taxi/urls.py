# taxi/urls.py
from django.urls import path
from . import views

# This is required for the namespace to work
app_name = "taxi"

urlpatterns = [
    # This path matches the root URL "http://12_7.0.0.1:8000/"
    path("", views.index, name="index"),
]
