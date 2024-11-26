from django.http import HttpRequest, HttpResponse
from .models import Car, Driver, Manufacturer
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacture = Manufacturer.objects.count()
    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacture,
    }
    return render(request, "taxi/index.html", context=context)
