from typing import Any

from django.shortcuts import render
from django.http import HttpRequest

from .models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> Any:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return render(
        request,
        template_name="taxi/index.html",
        context=context,
    )
