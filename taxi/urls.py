from django.urls import path

from taxi.views import index, manufacturers


urlpatterns = [
    path("", index, name="index"),
    path("manufacturer", manufacturers, name="manufacturer")
]

app_name = "taxi"
