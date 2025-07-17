from taxi.views import index
from django.urls import path, include

app_name = "taxi"
urlpatterns = [
    path("", index, name="index")
]
