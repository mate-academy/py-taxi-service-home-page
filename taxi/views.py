from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Car, Manufacturer, Driver


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    content = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", content)
