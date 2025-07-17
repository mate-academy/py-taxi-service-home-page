from taxi.views import index
from django.urls import path, include

urlpatterns = [
    path("", index, name="index")
]

app_name = "taxi"
