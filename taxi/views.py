from django.http import HttpRequest
from django.shortcuts import render

from taxi.models import Manufacturer, Driver, Car


def index(request: HttpRequest) -> object:
    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": Driver.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
            "num_cars": Car.objects.count(),
        },
    )
