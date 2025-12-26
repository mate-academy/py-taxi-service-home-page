from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


def index(request):
    num_of_drivers = Driver.objects.count()
    num_of_cars = Car.objects.count()
    num_of_manufacturers = Manufacturer.objects.count()

    context = {
        "num_of_drivers": num_of_drivers,
        "num_of_cars": num_of_cars,
        "num_of_manufacturers": num_of_manufacturers
    }

    return render(request, "taxi/index.html", context=context)
