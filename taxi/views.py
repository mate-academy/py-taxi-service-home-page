from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from taxi.models import Manufacturer, Driver, Car


def index(request: HttpRequest) -> HttpResponse:
    num_manufacturers = Manufacturer.objects.all().count()
    num_drivers = Driver.objects.all().count()
    num_cars = Car.objects.all().count()
    context = {
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context)
