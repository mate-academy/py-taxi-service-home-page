from django.shortcuts import render

from taxi.models import Car, Driver, Manufacturer


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers
    }
    return render(request, "taxi/index.html", context=context)
