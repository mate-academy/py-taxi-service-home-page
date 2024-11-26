from django.shortcuts import render
from django.http import HttpRequest
from .models import Driver, Manufacturer, Car


def index(request: HttpRequest):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    taxi_content = {"num_drivers": num_drivers,
                    "num_cars": num_cars,
                    "num_manufacturers": num_manufacturers}
    return render(request, "taxi/index.html"
                  , context=taxi_content)
