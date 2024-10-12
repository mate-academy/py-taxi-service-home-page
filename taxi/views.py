from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_Manufacturers = Manufacturer.objects.count()

    context = {
    "num_drivers": num_drivers,
    "num_cars": num_cars,
    "num_Manufacturers": num_Manufacturers,
    }

    return render (request, "taxi/index.html", context=context)
