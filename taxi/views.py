from django.shortcuts import render
from taxi.models import Manufacturer, Driver, Car
from typing import Any


def index(request) -> Any:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return render(
        request,
        "taxi/index.html",
        {
            "num_drivers": num_drivers,
            "num_manufacturers": num_manufacturers,
            "num_cars": num_cars,
        },
    )
