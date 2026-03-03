from django.urls import path

from taxi import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),
    path("manufacturers/", views.ManufacturerListView.as_view(),
         name="manufacturer_list"),
    path("cars/", views.CarListView.as_view(), name="car_list"),
    path("drivers/", views.DriverListView.as_view(), name="driver_list"),
]
