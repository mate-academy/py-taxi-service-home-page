from django.http import HttpResponse
from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_of_manufacturers = Manufacturer.objects.count()
    num_of_cars = Car.objects.count()
    context = {
        "num_cars": num_of_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_of_manufacturers,
    }
    return render(request, "taxi/index.html", context=context)
