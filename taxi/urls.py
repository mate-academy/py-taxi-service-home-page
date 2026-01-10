from django.urls import path

from taxi.views import index


urlpatterns = [
    path("", index)
]

app_name = "taxi"
