from django.urls import path

from taxi.views import index

urlpatterns = [
    path("http://127.0.0.1:8000/", index, name="index"),
]

app_name = "taxi"
