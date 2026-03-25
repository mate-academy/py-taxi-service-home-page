from django.urls import path

from taxi.views import index, manufacturers

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", manufacturers, name="manufacturers"),
    # path("", index, name="index"),
    # path("", index, name="index"),
]

app_name = "taxi"
