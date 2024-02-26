from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufactures = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufactures,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)
