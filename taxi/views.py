from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count(),
    num_manufacturers = Manufacturer.objects.count(),
    num_cars = Car.objects.count(),
    context = {
        "num_drivers": num_drivers[0],
        "num_manufacturers": num_manufacturers[0],
        "num_cars": num_cars[0],
    }
    return render(request, "taxi/index.html", context)
