from django.http import HttpRequest, HttpResponse

from taxi.models import Car, Manufacturer, Driver

from django.shortcuts import render


MENU = ["Home page", "Manufacturers", "Cars", "Drivers"]
EMPTY_MENU = {item: "" for item in MENU}


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "menu": EMPTY_MENU,
    }
    return render(request, "taxi/index.html", context=context)
