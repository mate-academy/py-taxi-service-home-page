from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Car.objects.count(),
        "num_manufacturers": Driver.objects.count(),
        "num_cars": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context)
