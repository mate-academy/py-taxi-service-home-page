from django.urls import path
from rest_framework.urls import app_name

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "taxi"
