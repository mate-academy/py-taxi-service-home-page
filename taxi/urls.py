from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="home"),
]

app_name = "taxi"
