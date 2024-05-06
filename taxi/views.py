from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "now": now,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }

    return render(request, "taxi/index.html", context=context)
