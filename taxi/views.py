from django.http import HttpRequest
from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest):
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers
    }
    return render(request, "taxi/index.html", context)
