from django.urls import path, include
from taxi.views import index


urlpatterns = [
    path("", index, name="index")
]

app_name = "taxi"
