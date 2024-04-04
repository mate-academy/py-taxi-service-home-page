from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Driver, Manufacturer, Car


def index(request: HttpRequest):
    print()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_drivers = Driver.objects.count()
    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers,
    }
    return render(request, "taxi/index.html", context=context)
