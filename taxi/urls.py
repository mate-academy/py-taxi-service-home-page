from django.urls import path
from . import views

app_name = "taxi"  # Add this line

urlpatterns = [
    path("", views.index, name="index"),
    # Add other paths as needed
]
