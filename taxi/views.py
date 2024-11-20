from django.shortcuts import render
from django.views.generic import ListView

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    data_to_template = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", data_to_template)


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
