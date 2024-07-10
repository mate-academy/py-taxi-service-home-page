from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_cars = Car.objects.all().count()
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
