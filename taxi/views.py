from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count()
    }
    return render(request, "taxi/index.html", context=context)
