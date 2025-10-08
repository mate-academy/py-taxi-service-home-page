from django.urls import path
from .views import index, ManufacturerListView

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    # Złamana długa linia (poprawka dla E501)
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
]
