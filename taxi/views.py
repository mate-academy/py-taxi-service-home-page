from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from taxi.models import Manufacturer, Car, Driver


def index(request: HttpRequest) -> HttpResponse:
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()

    context = {
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
        "num_drivers": num_drivers,
    }

    return render(request, "taxi/index.html", context=context)
