from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(req: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(req, "taxi/index.html", context)
