from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Manufacturer, Driver


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    menu = {
        item: "#" for item in ["Home page", "Manufacturers", "Cars", "Drivers"]
    }

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "menu": menu,
    }
    return render(request, "taxi/index.html", context=context)
