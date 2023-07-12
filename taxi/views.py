from django.http import HttpResponse
from django.shortcuts import render

from taxi import models


def index(request) -> HttpResponse:
    num_drivers = models.Driver.objects.count()
    num_manufacturers = models.Manufacturer.objects.count()
    num_cars = models.Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(request, "taxi/index.html", context=context)
