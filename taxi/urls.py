from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
    # path("taxi/", include("taxi.urls", namespace="taxi")),
]

app_name = "taxi"
