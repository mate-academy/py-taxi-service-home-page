from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import taxi
from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)


def manufacturers_view(request):
    return render(request, "taxi/manufacturers.html")


def cars_view(request):
    return render(request, "taxi/cars.html")


def drivers_view(request):
    return render(request, "taxi/drivers.html")
