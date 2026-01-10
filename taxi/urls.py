from django.urls import path

from taxi.views import index, manufacturer_list, car_list, driver_list

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", manufacturer_list, name="manufacturer-list"),
    path("cars/", car_list, name="car-list"),
    path("drivers/", driver_list, name="driver-list"),

]

app_name = "taxi"
