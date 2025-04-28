from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Driver, Manufacturer


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars
    }

    return render(request, "taxi/index.html", context)

def manufacturer_list(request):
    return HttpResponse("Manufacturer List Placeholder")

def car_list(request):
    return HttpResponse("Car List Placeholder")

def driver_list(request):
    return HttpResponse("Driver List Placeholder")