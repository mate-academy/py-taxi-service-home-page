from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from taxi.models import Car, Driver, Manufacturer


def index(requests: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return render(
        requests, "taxi/index.html",
        {"num_drivers": num_drivers,
         "num_manufacturers": num_manufacturers,
         "num_cars": num_cars}
    )
