from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }
    return render(
        request,
        "taxi/index.html",
        context
    )
