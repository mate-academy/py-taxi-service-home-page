from django.urls import path

from taxi.views import index


urlpatterns = [
    path("", index, name="index"),
    path("index/", index, name="index"),
]

app_name = "taxi"
