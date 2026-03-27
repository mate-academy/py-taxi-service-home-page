from django.urls import path

from taxi.views import index


urlpatterns = [
    path(route="", view=index, name="index"),
]

app_name = "taxi"
