from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacts = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers": num_drivers,
        "num_manufacts": num_manufacts,
        "num_cars": num_cars,
    }
    return render(request, "taxi/index.html", context=context)
