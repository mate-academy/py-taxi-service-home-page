from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "car_count": Car.objects.count(),
        "driver_count": Driver.objects.count(),
        "manufacturer_count": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context)
