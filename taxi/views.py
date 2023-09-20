from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers,
    }
    return render(request, "taxi/index.html", context=context)
