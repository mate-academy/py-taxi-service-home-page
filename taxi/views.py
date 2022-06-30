from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    drivers = Driver.objects.count()
    manufacturers = Manufacturer.objects.count()
    cars = Car.objects.count()
    context = {
        'drivers': drivers,
        'manufacturers': manufacturers,
        'cars': cars
    }
    return render(request, "taxi/index.html", context=context)
