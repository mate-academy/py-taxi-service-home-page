from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_of_drivers = Driver.objects.count()
    num_of_manufacturers = Manufacturer.objects.count()
    num_of_cars = Car.objects.count()

    context = {
        "num_of_drivers": num_of_drivers,
        "num_of_manufacturers": num_of_manufacturers,
        "num_of_cars": num_of_cars
    }
    return render(request, "taxi/index.html", context=context)
