from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers: int = Manufacturer.objects.count()
    num_cars: int = Car.objects.count()

    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": num_drivers,
            "num_manufacturers": num_manufacturers,
            "num_cars": num_cars
        }
    )
