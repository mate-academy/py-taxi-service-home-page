from django.http import HttpRequest
from django.shortcuts import render

from .models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> render:
    context = {
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_drivers": Driver.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)
