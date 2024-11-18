from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "drivers": num_drivers,
        "manufacturers": num_manufacturers,
        "cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)
