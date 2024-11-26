from django.urls import path
from taxi.views import index

urlpatterns = [
    path("home", index, name="index"),
]

app_name = "taxi"
