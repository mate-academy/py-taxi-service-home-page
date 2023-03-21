from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render
from taxi.models import Driver, Car, Manufacturer


def index(request: Request) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context=context)
