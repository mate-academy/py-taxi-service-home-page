from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Driver, Manufacturer, Car


def index(response: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(response, "taxi/index.html", context)
