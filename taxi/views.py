from django.http import HttpResponse, HttpRequest
from .models import Car, Manufacturer, Driver
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
