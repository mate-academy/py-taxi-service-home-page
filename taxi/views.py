from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Manufacturer, Driver


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": Driver.objects.all().count(),
            "num_manufacturers": Manufacturer.objects.all().count(),
            "num_cars": Car.objects.all().count(),
        },
    )


def drivers(request: HttpRequest) -> HttpResponse:
    return render(request, "taxi/drivers.html")


def cars(request: HttpRequest) -> HttpResponse:
    return render(request, "taxi/cars.html")


def manufactures(request: HttpRequest) -> HttpResponse:
    return render(request, "taxi/manufactures.html")
