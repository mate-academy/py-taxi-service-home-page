from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)


def manufacturers(request: HttpRequest) -> HttpResponse:
    context = {
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/manufacturers.html", context=context)
