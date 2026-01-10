from django.shortcuts import render
from .models import Driver, Car, Manufacturer


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    return render(request, "taxi/index.html", {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    })


def manufacturers(request):
    return render(request, "taxi/manufacturers.html")


def cars(request):
    return render(request, "taxi/cars.html")


def drivers(request):
    return render(request, "taxi/drivers.html")
