from django.urls import path

from taxi.views import index

app_name = "catalog"
urlpatterns = [
    path("index/", index, name="index"),
]
