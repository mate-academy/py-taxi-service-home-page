from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "taxi/index.html",
        {
            "num_drivers": Driver.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
            "num_cars": Car.objects.count(),
        },
    )
