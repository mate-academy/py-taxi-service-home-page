from django.urls import include, path

from taxi.views import index

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
]
