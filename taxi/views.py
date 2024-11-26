from django.shortcuts import render

from taxi.models import Manufacturer, Driver, Car


def index(request):
    """View function for home page of site."""

    num_manufacturers = Manufacturer.objects.count()
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers,
        "num_cars": num_cars,
    }

    return render(request, "taxi/index.html", context)
