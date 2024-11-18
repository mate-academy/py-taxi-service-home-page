from django.urls import path, include
from .views import index

app_name = "taxi"

urlpatterns = [
    path("", index, name="index")
]
