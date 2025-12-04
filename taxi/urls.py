# taxi/urls.py

from django.urls import path
from taxi.views import index, ManufacturerListView

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view()
         , name="manufacturer-list"),
]
