from django.shortcuts import render
from taxi.models import Manufacturer, Car, Driver


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturer = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturer,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context=context)
