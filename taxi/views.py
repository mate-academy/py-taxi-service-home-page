from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cars": Car.objects.count(),
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)
