from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    drivers = Driver.objects.count()
    manufacturers = Manufacturer.objects.count()
    cars = Car.objects.count()
    context = {
        "drivers": drivers,
        "manufacturers": manufacturers,
        "cars": cars,
    }
    return render(request, "taxi/index.html", context=context)
