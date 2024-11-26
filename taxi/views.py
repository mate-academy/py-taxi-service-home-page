from django.http import HttpRequest
from .models import Driver, Manufacturer, Car
from django.shortcuts import render


def index(request: HttpRequest) -> HttpRequest:
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    return render(request, "taxi/index.html", context={
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    })
